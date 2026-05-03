"""
EPUB processing routes:
  POST /epub/extract           — parse EPUB → persist Book + Chapters to DB
  POST /epub/summarize         — add AI summaries for included chapters
  POST /epub/marp              — fetch from DB → Marp presentation
  GET  /epub/llm/status        — check Ollama connectivity
  GET  /epub/chapters          — list all chapters for a book
  POST /epub/chapters/include  — toggle include flag on chapters
"""
import logging
import os
from fastapi import APIRouter, Depends, HTTPException

from src.application.use_cases.epub_use_cases import (
    CheckLLMConnectionUseCase,
    ExtractEpubUseCase,
    GenerateMarpUseCase,
    ListChaptersUseCase,
    SetExcludedSectionsUseCase,
    SummarizeEpubUseCase,
)
from src.application.dtos.epub_dtos import (
    ExtractEpubRequest,
    GenerateMarpRequest,
    ListChaptersRequest,
    SetExcludedSectionsRequest,
    SummarizeEpubRequest,
)
from src.infrastructure.ai.ollama_agent import AIAgent
from src.infrastructure.database.session import get_session
from src.infrastructure.epub.epub_extractor import EPUBExtractor
from src.infrastructure.export.marp_exporter import MarpExporter
from src.infrastructure.repositories.postgres_repository import PostgresBookRepository
from app.api.schemas.schemas import (
    ChaptersListResponse,
    ExtractRequest, ExtractResponse,
    LLMStatusResponse,
    MarpRequest, MarpResponse,
    SetInclusionRequest, SetInclusionResponse,
    SummarizeRequest, SummarizeResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/epub", tags=["epub"])


def _extract_use_case(session=Depends(get_session)) -> ExtractEpubUseCase:
    return ExtractEpubUseCase(
        extractor=EPUBExtractor(),
        repository=PostgresBookRepository(session),
    )


def _summarize_use_case(session=Depends(get_session)) -> SummarizeEpubUseCase:
    return SummarizeEpubUseCase(
        ai_agent=AIAgent(),
        repository=PostgresBookRepository(session),
    )


def _marp_use_case(session=Depends(get_session)) -> GenerateMarpUseCase:
    return GenerateMarpUseCase(
        marp_exporter=MarpExporter(),
        repository=PostgresBookRepository(session),
    )


def _llm_use_case() -> CheckLLMConnectionUseCase:
    return CheckLLMConnectionUseCase()


def _list_chapters_use_case(session=Depends(get_session)) -> ListChaptersUseCase:
    return ListChaptersUseCase(repository=PostgresBookRepository(session))


def _set_inclusion_use_case(session=Depends(get_session)) -> SetExcludedSectionsUseCase:
    return SetExcludedSectionsUseCase(repository=PostgresBookRepository(session))


@router.post("/extract", response_model=ExtractResponse)
async def extract_epub(
    body: ExtractRequest,
    use_case: ExtractEpubUseCase = Depends(_extract_use_case),
):
    """Parse an EPUB file and persist Book + Chapter entities to the database."""
    if not os.path.exists(body.epub_path):
        raise HTTPException(status_code=404, detail=f"EPUB file not found: {body.epub_path}")
    try:
        response = use_case.execute(
            ExtractEpubRequest(
                epub_path=body.epub_path,
                book_name=body.book_name,
                images_output_dir=body.images_output_dir,
                language=body.language,
                author=body.author,
            )
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"book_id": response.book_id, "total_chapters": response.total_chapters, "total_content_chars": response.total_content_chars}


@router.post("/summarize", response_model=SummarizeResponse)
async def summarize_epub(
    body: SummarizeRequest,
    use_case: SummarizeEpubUseCase = Depends(_summarize_use_case),
):
    """Generate AI summaries for included chapters (requires Ollama).

    Optionally pass ``chapter_ids`` to restrict summarisation to a specific subset.
    """
    try:
        response = use_case.execute(
            SummarizeEpubRequest(book_id=body.book_id, chapter_ids=body.chapter_ids)
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"book_id": response.book_id, "chapters_summarized": response.chapters_summarized}


@router.post("/marp", response_model=MarpResponse)
async def generate_marp(
    body: MarpRequest,
    use_case: GenerateMarpUseCase = Depends(_marp_use_case),
):
    """Fetch book data from the database and generate a Marp presentation."""
    try:
        response = use_case.execute(
            GenerateMarpRequest(
                book_id=body.book_id,
                marp_output_path=body.marp_output,
                title=body.title,
                include_summaries=body.include_summaries,
                include_content=body.include_content,
                max_depth=body.max_depth,
            )
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"marp_output": response.marp_output_path}


@router.get("/llm/status", response_model=LLMStatusResponse)
async def llm_status(use_case: CheckLLMConnectionUseCase = Depends(_llm_use_case)):
    """Check whether the Ollama LLM service is reachable."""
    response = use_case.execute()
    return {"connected": response.connected, "host": response.host, "model": response.model}


@router.get("/chapters", response_model=ChaptersListResponse)
async def list_chapters(
    book_id: str,
    use_case: ListChaptersUseCase = Depends(_list_chapters_use_case),
):
    """Return a flat, ordered list of all chapters for a book."""
    try:
        response = use_case.execute(ListChaptersRequest(book_id=book_id))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {
        "book_id": response.book_id,
        "total": len(response.chapters),
        "chapters": [
            {
                "id": ch.id,
                "title": ch.title,
                "number": ch.number,
                "include": ch.include,
                "has_summary": ch.has_summary,
                "chapter_id": ch.chapter_id,
            }
            for ch in response.chapters
        ],
    }


@router.post("/chapters/include", response_model=SetInclusionResponse)
async def set_chapter_inclusion(
    body: SetInclusionRequest,
    use_case: SetExcludedSectionsUseCase = Depends(_set_inclusion_use_case),
):
    """Toggle the ``include`` flag on a list of chapters.

    Set ``include=false`` to exclude chapters from AI summarisation;
    ``include=true`` to re-include them.
    """
    try:
        response = use_case.execute(
            SetExcludedSectionsRequest(
                book_id=body.book_id,
                chapter_ids=body.chapter_ids,
                include=body.include,
            )
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"book_id": response.book_id, "updated_count": response.updated_count}

