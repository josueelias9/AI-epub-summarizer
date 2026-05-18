"""
Routes for Marp generation and LLM status.
"""

import logging
from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep
from src.application.use_cases.epub_use_cases import (
    CheckLLMConnectionUseCase,
    GenerateMarpUseCase,
)
from src.application.dtos.epub_dtos import GenerateMarpRequest
from src.infrastructure.export.marp_exporter import MarpExporter
from src.infrastructure.repositories.postgres_repository import PostgresBookRepository
from src.infrastructure.ai.ollama_agent import AIAgent
from src.infrastructure.database.models import MarpRequest, MarpResponse, LLMStatusResponse

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/epub", tags=["epub"])

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
