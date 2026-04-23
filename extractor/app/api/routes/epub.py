"""
EPUB processing routes: extract structure and generate Marp presentation.
"""
import os
from fastapi import APIRouter, Depends, HTTPException

from app.application.use_cases.epub_use_cases import ExtractEpubUseCase, GenerateMarpUseCase
from app.infrastructure.epub.epub_extractor import EPUBExtractor
from app.infrastructure.ai.ollama_agent import AIAgent
from app.infrastructure.export.marp_exporter import MarpExporter
from app.core.config import settings
from app.api.schemas.schemas import ExtractRequest, ExtractResponse, MarpRequest, MarpResponse

router = APIRouter(prefix="/epub", tags=["epub"])


def _extract_use_case() -> ExtractEpubUseCase:
    return ExtractEpubUseCase(
        extractor=EPUBExtractor(),
        ai_agent=AIAgent(),
    )


def _marp_use_case() -> GenerateMarpUseCase:
    return GenerateMarpUseCase(marp_exporter=MarpExporter())


def _default_json_path() -> str:
    return os.path.join(settings.OUTPUT_PATH, "book_with_summaries.json")


def _default_epub_path() -> str:
    return os.path.join(settings.INPUT_PATH, settings.EPUB_FILE)


@router.post("/extract", response_model=ExtractResponse)
async def extract_epub(
    body: ExtractRequest,
    use_case: ExtractEpubUseCase = Depends(_extract_use_case),
):
    """
    Extract the hierarchical structure from an EPUB file and save it as JSON.
    Optionally generates AI summaries via Ollama (slow — requires Ollama running).
    """
    epub_path = body.epub_path or _default_epub_path()
    json_output = body.json_output or _default_json_path()

    if not os.path.exists(epub_path):
        raise HTTPException(status_code=404, detail=f"EPUB file not found: {epub_path}")

    try:
        structure = use_case.execute(
            epub_path=epub_path,
            json_output=json_output,
            generate_summaries=body.generate_summaries,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    stats = use_case.get_statistics(structure)
    return ExtractResponse(
        json_output=json_output,
        total_sections=stats["total_sections"],
        total_content_chars=stats["total_content_chars"],
        sections_with_summaries=stats["sections_with_summaries"],
    )


@router.post("/marp", response_model=MarpResponse)
async def generate_marp(
    body: MarpRequest,
    use_case: GenerateMarpUseCase = Depends(_marp_use_case),
):
    """
    Generate a Marp markdown presentation from a previously extracted JSON structure.
    Run /epub/extract first if the JSON does not exist yet.
    """
    json_path = body.json_path or _default_json_path()
    marp_output = body.marp_output or os.path.join(settings.OUTPUT_PATH, "book_presentation.md")

    if not os.path.exists(json_path):
        raise HTTPException(
            status_code=404,
            detail=f"JSON structure not found: {json_path}. Run POST /epub/extract first.",
        )

    try:
        use_case.execute(
            json_path=json_path,
            marp_output_path=marp_output,
            title=body.title,
            include_summaries=body.include_summaries,
            include_content=body.include_content,
            max_depth=body.max_depth,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return MarpResponse(marp_output=marp_output)
