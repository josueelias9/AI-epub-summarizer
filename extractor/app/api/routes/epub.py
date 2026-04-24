"""
EPUB processing routes:
  POST /epub/extract          — parse EPUB → structure
  POST /epub/summarize        — add AI summaries (requires Ollama)
  POST /epub/marp             — structure → Marp presentation
  GET  /epub/llm/status       — check Ollama connectivity
  GET  /epub/sections         — list all sections
  POST /epub/sections/exclude — set excluded section IDs
"""
import logging
import os
from fastapi import APIRouter, Depends, HTTPException

from app.application.use_cases.epub_use_cases import (
    ExtractEpubUseCase,
    SummarizeEpubUseCase,
    GenerateMarpUseCase,
    CheckLLMConnectionUseCase,
    ListSectionsUseCase,
    SetExcludedSectionsUseCase,
)
from app.application.dtos.epub_dtos import (
    ExtractEpubRequest,
    SummarizeEpubRequest,
    GenerateMarpRequest,
    ListSectionsRequest,
    SetExcludedSectionsRequest,
)
from app.infrastructure.epub.epub_extractor import EPUBExtractor
from app.infrastructure.ai.ollama_agent import AIAgent
from app.infrastructure.export.marp_exporter import MarpExporter
from app.infrastructure.repositories.local_repository import LocalBookRepository
from app.api.schemas.schemas import (
    ExtractRequest, ExtractResponse,
    SummarizeRequest, SummarizeResponse,
    MarpRequest, MarpResponse,
    LLMStatusResponse,
    SectionsListResponse,
    SetExcludedRequest, SetExcludedResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/epub", tags=["epub"])


def _extract_use_case() -> ExtractEpubUseCase:
    return ExtractEpubUseCase(extractor=EPUBExtractor(), repository=LocalBookRepository())


def _summarize_use_case() -> SummarizeEpubUseCase:
    return SummarizeEpubUseCase(ai_agent=AIAgent(), repository=LocalBookRepository())


def _marp_use_case() -> GenerateMarpUseCase:
    return GenerateMarpUseCase(marp_exporter=MarpExporter(), repository=LocalBookRepository())


def _llm_use_case() -> CheckLLMConnectionUseCase:
    return CheckLLMConnectionUseCase(ai_agent=AIAgent())


def _list_sections_use_case() -> ListSectionsUseCase:
    return ListSectionsUseCase(repository=LocalBookRepository())


def _set_excluded_use_case() -> SetExcludedSectionsUseCase:
    return SetExcludedSectionsUseCase(repository=LocalBookRepository())


@router.post("/extract", response_model=ExtractResponse)
async def extract_epub(
    body: ExtractRequest,
    use_case: ExtractEpubUseCase = Depends(_extract_use_case),
):
    """Parse an EPUB file and save its hierarchical structure."""
    if not os.path.exists(body.epub_path):
        raise HTTPException(status_code=404, detail=f"EPUB file not found: {body.epub_path}")

    images_output_dir = os.path.join(os.path.dirname(os.path.abspath(body.json_output)), "images")
    try:
        response = use_case.execute(ExtractEpubRequest(
            epub_path=body.epub_path,
            book_key=body.json_output,
            images_output_dir=images_output_dir,
        ))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "json_output": response.book_key,
        "total_sections": response.total_sections,
        "total_content_chars": response.total_content_chars,
        "sections_with_summaries": response.sections_with_summaries,
    }


@router.post("/summarize", response_model=SummarizeResponse)
async def summarize_epub(
    body: SummarizeRequest,
    use_case: SummarizeEpubUseCase = Depends(_summarize_use_case),
):
    """Add AI-generated summaries to an existing structure (requires Ollama)."""
    try:
        response = use_case.execute(SummarizeEpubRequest(book_key=body.json_path))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"json_path": response.book_key, "sections_summarized": response.sections_summarized}


@router.post("/marp", response_model=MarpResponse)
async def generate_marp(
    body: MarpRequest,
    use_case: GenerateMarpUseCase = Depends(_marp_use_case),
):
    """Generate a Marp markdown presentation from a previously extracted structure."""
    try:
        response = use_case.execute(GenerateMarpRequest(
            book_key=body.json_path,
            marp_output_path=body.marp_output,
            title=body.title,
            include_summaries=body.include_summaries,
            include_content=body.include_content,
            max_depth=body.max_depth,
        ))
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


@router.get("/sections", response_model=SectionsListResponse)
async def list_sections(
    book_key: str,
    use_case: ListSectionsUseCase = Depends(_list_sections_use_case),
):
    """Return a flat list of all sections for a previously extracted book structure."""
    try:
        response = use_case.execute(ListSectionsRequest(book_key=book_key))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "book_key": response.book_key,
        "total": len(response.sections),
        "sections": [
            {"id": s.id, "title": s.title, "depth": s.depth, "excluded": s.excluded, "has_summary": s.has_summary}
            for s in response.sections
        ],
    }


@router.post("/sections/exclude", response_model=SetExcludedResponse)
async def set_excluded_sections(
    body: SetExcludedRequest,
    use_case: SetExcludedSectionsUseCase = Depends(_set_excluded_use_case),
):
    """Set which sections are excluded from summarization and Marp generation.

    Provide the list of section IDs (e.g. '1', '1.2', '3.1') to exclude.
    All other sections will be treated as included.
    """
    try:
        response = use_case.execute(SetExcludedSectionsRequest(
            book_key=body.book_key,
            excluded_ids=body.excluded_ids,
        ))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"book_key": response.book_key, "excluded_count": response.excluded_count}


