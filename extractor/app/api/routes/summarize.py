"""
Routes for AI summarization of EPUB chapters.
"""

import logging
from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep
from src.application.use_cases.epub_use_cases import SummarizeEpubUseCase
from src.application.dtos.epub_dtos import SummarizeEpubRequest
from src.infrastructure.ai.ollama_agent import AIAgent
from src.infrastructure.repositories.postgres_repository import PostgresBookRepository
from src.infrastructure.database.models import SummarizeRequest, SummarizeResponse

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/epub", tags=["epub"])

@router.post("/summarize", response_model=SummarizeResponse)
async def summarize_epub(
    body: SummarizeRequest,
    session: SessionDep,
):
    """Generate AI summaries for included chapters (requires Ollama).

    Optionally pass ``chapter_ids`` to restrict summarisation to a specific subset.
    """
    use_case = SummarizeEpubUseCase(
        ai_agent=AIAgent(),
        repository=PostgresBookRepository(session),
    )
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
