"""
EPUB processing routes:
  POST /epub/extract    — parse EPUB → JSON structure
  POST /epub/summarize  — add AI summaries to existing JSON (requires Ollama)
  POST /epub/marp       — JSON structure → Marp presentation
  GET  /epub/llm/status — check Ollama connectivity
"""
import logging
import os
from fastapi import APIRouter, Depends, HTTPException

from app.application.use_cases.epub_use_cases import (
    ExtractEpubUseCase,
    SummarizeEpubUseCase,
    GenerateMarpUseCase,
    CheckLLMConnectionUseCase,
)
from app.infrastructure.epub.epub_extractor import EPUBExtractor
from app.infrastructure.ai.ollama_agent import AIAgent
from app.infrastructure.export.marp_exporter import MarpExporter
from app.api.schemas.schemas import (
    ExtractRequest, ExtractResponse,
    SummarizeRequest, SummarizeResponse,
    MarpRequest, MarpResponse,
    LLMStatusResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/epub", tags=["epub"])


def _extract_use_case() -> ExtractEpubUseCase:
    return ExtractEpubUseCase(extractor=EPUBExtractor())


def _summarize_use_case() -> SummarizeEpubUseCase:
    return SummarizeEpubUseCase(ai_agent=AIAgent())


def _marp_use_case() -> GenerateMarpUseCase:
    return GenerateMarpUseCase(marp_exporter=MarpExporter())


def _llm_use_case() -> CheckLLMConnectionUseCase:
    return CheckLLMConnectionUseCase(ai_agent=AIAgent())


@router.post("/extract", response_model=ExtractResponse)
async def extract_epub(
    body: ExtractRequest,
    use_case: ExtractEpubUseCase = Depends(_extract_use_case),
):
    """Parse an EPUB file and save its hierarchical structure as JSON."""
    if not os.path.exists(body.epub_path):
        raise HTTPException(status_code=404, detail=f"EPUB file not found: {body.epub_path}")

    try:
        structure = use_case.execute(epub_path=body.epub_path, json_output=body.json_output)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    stats = use_case.get_statistics(structure)
    return ExtractResponse(
        json_output=body.json_output,
        total_sections=stats["total_sections"],
        total_content_chars=stats["total_content_chars"],
        sections_with_summaries=stats["sections_with_summaries"],
    )


@router.post("/summarize", response_model=SummarizeResponse)
async def summarize_epub(
    body: SummarizeRequest,
    use_case: SummarizeEpubUseCase = Depends(_summarize_use_case),
):
    """Add AI-generated summaries to an existing JSON structure (requires Ollama)."""
    if not os.path.exists(body.json_path):
        raise HTTPException(
            status_code=404,
            detail=f"JSON structure not found: {body.json_path}. Run POST /epub/extract first.",
        )

    try:
        structure = use_case.execute(json_path=body.json_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    count = sum(1 for _ in _iter_sections(structure) if _.get("summary"))
    return SummarizeResponse(json_path=body.json_path, sections_summarized=count)


@router.post("/marp", response_model=MarpResponse)
async def generate_marp(
    body: MarpRequest,
    use_case: GenerateMarpUseCase = Depends(_marp_use_case),
):
    """Generate a Marp markdown presentation from a previously extracted JSON structure."""
    if not os.path.exists(body.json_path):
        raise HTTPException(
            status_code=404,
            detail=f"JSON structure not found: {body.json_path}. Run POST /epub/extract first.",
        )

    try:
        use_case.execute(
            json_path=body.json_path,
            marp_output_path=body.marp_output,
            title=body.title,
            include_summaries=body.include_summaries,
            include_content=body.include_content,
            max_depth=body.max_depth,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return MarpResponse(marp_output=body.marp_output)


@router.get("/llm/status", response_model=LLMStatusResponse)
async def llm_status(use_case: CheckLLMConnectionUseCase = Depends(_llm_use_case)):
    """Check whether the Ollama LLM service is reachable."""
    return use_case.execute()


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _iter_sections(structure: dict):
    for info in structure.values():
        yield info
        if info.get("subsections"):
            yield from _iter_sections(info["subsections"])

        yield info
        if info.get("subsections"):
            yield from _iter_sections(info["subsections"])

