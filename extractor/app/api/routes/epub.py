"""
EPUB processing routes:
  GET  /epub/books               — list all books
  POST /epub/upload              — upload & extract an EPUB file
  DELETE /epub/books/{book_id}   — delete book + chapters + epub file
  POST /epub/extract             — parse EPUB → persist Book + Chapters to DB
  POST /epub/summarize           — add AI summaries for included chapters
  POST /epub/marp                — fetch from DB → Marp presentation
  GET  /epub/llm/status          — check Ollama connectivity
  GET  /epub/chapters            — list all chapters for a book
  POST /epub/chapters/include    — toggle include flag on chapters
  GET  /epub/slides/{book_id}    — get chapters as slide data
"""

import logging
import os
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from typing import Optional

from src.application.use_cases.epub_use_cases import (
    CheckLLMConnectionUseCase,
    DeleteBookUseCase,
    ExtractEpubUseCase,
    GenerateMarpUseCase,
    GetSlidesUseCase,
    ListBooksUseCase,
    ListChaptersUseCase,
    SetExcludedSectionsUseCase,
    SummarizeEpubUseCase,
)
from src.application.dtos.epub_dtos import (
    DeleteBookRequest,
    ExtractEpubRequest,
    GenerateMarpRequest,
    GetSlidesRequest,
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
    BooksListResponse,
    ChaptersListResponse,
    DeleteBookResponse,
    ExtractRequest,
    ExtractResponse,
    LLMStatusResponse,
    MarpRequest,
    MarpResponse,
    SetInclusionRequest,
    SetInclusionResponse,
    SlideInfo,
    SlidesResponse,
    SummarizeRequest,
    SummarizeResponse,
    UploadEpubResponse,
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


def _list_books_use_case(session=Depends(get_session)) -> ListBooksUseCase:
    return ListBooksUseCase(repository=PostgresBookRepository(session))


def _delete_book_use_case(session=Depends(get_session)) -> DeleteBookUseCase:
    return DeleteBookUseCase(repository=PostgresBookRepository(session))


def _get_slides_use_case(session=Depends(get_session)) -> GetSlidesUseCase:
    return GetSlidesUseCase(repository=PostgresBookRepository(session))


@router.get("/books", response_model=BooksListResponse)
async def list_books(use_case: ListBooksUseCase = Depends(_list_books_use_case)):
    """Return all books stored in the database."""
    response = use_case.execute()
    return {
        "total": len(response.books),
        "books": [
            {"id": b.id, "name": b.name, "language": b.language, "author": b.author}
            for b in response.books
        ],
    }


@router.post("/upload", response_model=UploadEpubResponse)
async def upload_epub(
    file: UploadFile = File(...),
    book_name: Optional[str] = Form(default=None),
    use_case: ExtractEpubUseCase = Depends(_extract_use_case),
):
    """Upload an EPUB file, extract its structure and persist to the database."""
    safe_name = os.path.basename(file.filename or "book.epub")
    if not safe_name.lower().endswith(".epub"):
        raise HTTPException(status_code=400, detail="Only .epub files are accepted.")

    upload_dir = "/app/uploads"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, safe_name)

    contents = await file.read()
    with open(file_path, "wb") as fh:
        fh.write(contents)

    display_name = book_name or os.path.splitext(safe_name)[0]
    try:
        response = use_case.execute(
            ExtractEpubRequest(
                epub_path=file_path,
                book_name=display_name,
                images_output_dir="/app/output/images",
                save_epub_path=file_path,
            )
        )
    except Exception as e:
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "book_id": response.book_id,
        "book_name": display_name,
        "total_chapters": response.total_chapters,
    }


@router.delete("/books/{book_id}", response_model=DeleteBookResponse)
async def delete_book(
    book_id: str,
    use_case: DeleteBookUseCase = Depends(_delete_book_use_case),
):
    """Delete a book, its chapters, and the epub file from the filesystem."""
    try:
        response = use_case.execute(DeleteBookRequest(book_id=book_id))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"book_id": response.book_id, "success": response.success}


@router.get("/slides/{book_id}", response_model=SlidesResponse)
async def get_slides(
    book_id: str,
    use_case: GetSlidesUseCase = Depends(_get_slides_use_case),
):
    """Return included chapters as structured slide data for the frontend."""
    try:
        response = use_case.execute(GetSlidesRequest(book_id=book_id))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {
        "book_id": response.book_id,
        "book_name": response.book_name,
        "slides": [
            {
                "chapter_id": s.chapter_id,
                "title": s.title,
                "number": s.number,
                "summary": s.summary,
                "content": s.content,
                "images": s.images,
                "depth": s.depth,
            }
            for s in response.slides
        ],
    }


@router.post("/extract", response_model=ExtractResponse)
async def extract_epub(
    body: ExtractRequest,
    use_case: ExtractEpubUseCase = Depends(_extract_use_case),
):
    """Parse an EPUB file and persist Book + Chapter entities to the database."""
    if not os.path.exists(body.epub_path):
        raise HTTPException(
            status_code=404, detail=f"EPUB file not found: {body.epub_path}"
        )
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
    return {
        "book_id": response.book_id,
        "total_chapters": response.total_chapters,
        "total_content_chars": response.total_content_chars,
    }


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
    return {
        "book_id": response.book_id,
        "chapters_summarized": response.chapters_summarized,
    }


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
    return {
        "connected": response.connected,
        "host": response.host,
        "model": response.model,
    }


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
                chapter_numbers=body.chapter_numbers,
                include=body.include,
            )
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"book_id": response.book_id, "updated_count": response.updated_count}
