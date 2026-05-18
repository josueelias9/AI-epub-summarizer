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
from fastapi import APIRouter, HTTPException, UploadFile, File, Form
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
)
from src.application.dtos.epub_dtos import (
    DeleteBookRequest,
    ExtractEpubRequest,
    GenerateMarpRequest,
    GetSlidesRequest,
    ListChaptersRequest,
    SetExcludedSectionsRequest,
)
from app.api.deps import SessionDep
from src.infrastructure.ai.ollama_agent import AIAgent
from src.infrastructure.epub.epub_extractor import EPUBExtractor
from src.infrastructure.epub.sources.local_source import LocalFileSource
from src.infrastructure.epub.sources.upload_source import UploadedFileSource
from src.infrastructure.export.marp_exporter import MarpExporter
from src.infrastructure.repositories.postgres_repository import PostgresBookRepository
from src.infrastructure.repositories.summary_job_repository import SummaryJobRepository
from src.infrastructure.queue.rabbitmq import RabbitMQQueue
from src.infrastructure.database.models import (
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
    SlidesResponse,
    SummarizeRequest,
    SummarizeResponse,
    UploadEpubResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/epub", tags=["epub"])


@router.get("/books", response_model=BooksListResponse)
async def list_books(session: SessionDep):
    """Return all books stored in the database."""
    use_case = ListBooksUseCase(repository=PostgresBookRepository(session))
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
    session: SessionDep = ...,
):
    """Upload an EPUB file, extract its structure and persist to the database."""
    safe_name = os.path.basename(file.filename or "book.epub")
    if not safe_name.lower().endswith(".epub"):
        raise HTTPException(status_code=400, detail="Only .epub files are accepted.")
    contents = await file.read()
    use_case = ExtractEpubUseCase(
        source=UploadedFileSource(content=contents, filename=safe_name),
        extractor=EPUBExtractor(),
        repository=PostgresBookRepository(session),
    )
    display_name = book_name or os.path.splitext(safe_name)[0]
    try:
        response = use_case.execute(
            ExtractEpubRequest(
                epub_path=safe_name,
                book_name=display_name,
                images_output_dir="/app/output/images",
                save_epub_path=f"/app/uploads/{safe_name}",
            )
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "book_id": response.book_id,
        "book_name": display_name,
        "total_chapters": response.total_chapters,
    }


@router.delete("/books/{book_id}", response_model=DeleteBookResponse)
async def delete_book(
    book_id: str,
    session: SessionDep,
):
    """Delete a book, its chapters, and the epub file from the filesystem."""
    use_case = DeleteBookUseCase(repository=PostgresBookRepository(session))
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
    session: SessionDep,
):
    """Return included chapters as structured slide data for the frontend."""
    use_case = GetSlidesUseCase(repository=PostgresBookRepository(session))
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
    session: SessionDep,
):
    """Parse a local EPUB file and persist Book + Chapter entities to the database."""
    use_case = ExtractEpubUseCase(
        source=LocalFileSource(),
        extractor=EPUBExtractor(),
        repository=PostgresBookRepository(session),
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
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {
        "book_id": response.book_id,
        "total_chapters": response.total_chapters,
        "total_content_chars": response.total_content_chars,
    }


@router.post("/marp", response_model=MarpResponse)
async def generate_marp(
    body: MarpRequest,
    session: SessionDep,
):
    """Fetch book data from the database and generate a Marp presentation."""
    use_case = GenerateMarpUseCase(
        marp_exporter=MarpExporter(),
        repository=PostgresBookRepository(session),
    )
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
async def llm_status():
    """Check whether the Ollama LLM service is reachable."""
    use_case = CheckLLMConnectionUseCase(ai_agent=AIAgent())
    response = use_case.execute()
    return {
        "connected": response.connected,
        "host": response.host,
        "model": response.model,
    }


@router.get("/chapters", response_model=ChaptersListResponse)
async def list_chapters(
    book_id: str,
    session: SessionDep,
):
    """Return a flat, ordered list of all chapters for a book."""
    use_case = ListChaptersUseCase(repository=PostgresBookRepository(session))
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
    session: SessionDep,
):
    """Toggle the ``include`` flag on a list of chapters.

    Set ``include=false`` to exclude chapters from AI summarisation;
    ``include=true`` to re-include them.
    """
    use_case = SetExcludedSectionsUseCase(repository=PostgresBookRepository(session))
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
