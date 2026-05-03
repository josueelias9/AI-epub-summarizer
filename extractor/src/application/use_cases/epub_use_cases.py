"""
Use cases for EPUB extraction, AI summarisation, and Marp generation
(Clean Architecture — single responsibility per class).
"""
import logging
import os
from datetime import datetime
from typing import List, Optional

from src.application.ports.service_ports import (
    AIServicePort,
    BookRepositoryPort,
    EpubExtractorPort,
    MarpExporterPort,
)
from src.application.dtos.epub_dtos import (
    ChapterDTO,
    CheckLLMConnectionResponse,
    ExtractEpubRequest,
    ExtractEpubResponse,
    GenerateMarpRequest,
    GenerateMarpResponse,
    ListChaptersRequest,
    ListChaptersResponse,
    SetExcludedSectionsRequest,
    SetExcludedSectionsResponse,
    SummarizeEpubRequest,
    SummarizeEpubResponse,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Extract
# ---------------------------------------------------------------------------

class ExtractEpubUseCase:
    """Parse an EPUB file and persist Book + Chapter entities to the repository."""

    def __init__(self, extractor: EpubExtractorPort, repository: BookRepositoryPort):
        self._extractor = extractor
        self._repository = repository

    def execute(self, request: ExtractEpubRequest) -> ExtractEpubResponse:
        book, chapters = self._extractor.extract(
            request.epub_path,
            request.images_output_dir,
        )

        # Allow caller to override EPUB metadata
        if request.book_name:
            book.name = request.book_name
        if request.language:
            book.language = request.language
        if request.author:
            book.author = request.author

        self._repository.save_book(book)
        self._repository.save_chapters(chapters)

        total_chars = sum(len(ch.content) for ch in chapters)
        logger.info(
            "Extracted %d chapters (%d chars) for book %r",
            len(chapters), total_chars, book.id,
        )
        return ExtractEpubResponse(
            book_id=book.id,
            total_chapters=len(chapters),
            total_content_chars=total_chars,
        )


# ---------------------------------------------------------------------------
# Summarize
# ---------------------------------------------------------------------------

class SummarizeEpubUseCase:
    """Generate AI summaries for included chapters and persist them."""

    def __init__(self, ai_agent: AIServicePort, repository: BookRepositoryPort):
        self._ai_agent = ai_agent
        self._repository = repository

    def execute(self, request: SummarizeEpubRequest) -> SummarizeEpubResponse:
        logger.info("Starting summarisation for book %r", request.book_id)

        if request.chapter_ids:
            # Summarise a specific subset — still honour the include flag
            chapters = [
                ch
                for cid in request.chapter_ids
                if (ch := self._repository.get_chapter(cid)) is not None and ch.include
            ]
        else:
            # Summarise all chapters that are flagged for inclusion
            chapters = self._repository.get_chapters(request.book_id, include_only=True)

        count = 0
        for chapter in chapters:
            if not chapter.content:
                logger.info("Skipping chapter %r (no content)", chapter.id)
                continue
            logger.info("Summarising chapter %r — %s", chapter.id, chapter.title)
            summary = self._ai_agent.summarize_content(chapter.content)
            self._repository.update_chapter_summary(
                chapter_id=chapter.id,
                summary=summary,
                summary_date=datetime.utcnow(),
                ai_generated=True,
            )
            count += 1

        logger.info("Summarisation complete — %d chapters processed", count)
        return SummarizeEpubResponse(book_id=request.book_id, chapters_summarized=count)


# ---------------------------------------------------------------------------
# Generate Marp
# ---------------------------------------------------------------------------

class GenerateMarpUseCase:
    """Fetch book data from the repository and generate a Marp presentation."""

    def __init__(self, marp_exporter: MarpExporterPort, repository: BookRepositoryPort):
        self._marp_exporter = marp_exporter
        self._repository = repository

    def execute(self, request: GenerateMarpRequest) -> GenerateMarpResponse:
        book = self._repository.get_book(request.book_id)
        if book is None:
            raise ValueError(f"Book {request.book_id!r} not found. Run extract first.")

        chapters = self._repository.get_chapters(request.book_id)

        os.makedirs(os.path.dirname(request.marp_output_path) or ".", exist_ok=True)
        self._marp_exporter.export(
            book=book,
            chapters=chapters,
            output_path=request.marp_output_path,
            include_summaries=request.include_summaries,
            include_content=request.include_content,
            max_depth=request.max_depth,
        )
        return GenerateMarpResponse(marp_output_path=request.marp_output_path)


# ---------------------------------------------------------------------------
# Check LLM connection
# ---------------------------------------------------------------------------

class CheckLLMConnectionUseCase:
    """Verify that the Ollama LLM service is reachable."""

    def __init__(self, ai_agent: AIServicePort):
        self._ai_agent = ai_agent

    def execute(self) -> CheckLLMConnectionResponse:
        info = self._ai_agent.get_connection_info()
        logger.info("Checking LLM connection to %s (model: %s)", info["host"], info["model"])
        ok = self._ai_agent.test_connection()
        return CheckLLMConnectionResponse(connected=ok, host=info["host"], model=info["model"])


# ---------------------------------------------------------------------------
# List chapters
# ---------------------------------------------------------------------------

class ListChaptersUseCase:
    """Return a flat, ordered list of all chapters for a book."""

    def __init__(self, repository: BookRepositoryPort):
        self._repository = repository

    def execute(self, request: ListChaptersRequest) -> ListChaptersResponse:
        book = self._repository.get_book(request.book_id)
        if book is None:
            raise ValueError(f"Book {request.book_id!r} not found. Run extract first.")

        chapters = self._repository.get_chapters(request.book_id)
        dtos = [
            ChapterDTO(
                id=ch.id,
                title=ch.title,
                number=ch.number,
                include=ch.include,
                has_summary=bool(ch.summary),
                chapter_id=ch.chapter_id,
            )
            for ch in chapters
        ]
        return ListChaptersResponse(book_id=request.book_id, chapters=dtos)


# ---------------------------------------------------------------------------
# Set inclusion / exclusion
# ---------------------------------------------------------------------------

class SetExcludedSectionsUseCase:
    """Toggle the ``include`` flag on a set of chapters."""

    def __init__(self, repository: BookRepositoryPort):
        self._repository = repository

    def execute(self, request: SetExcludedSectionsRequest) -> SetExcludedSectionsResponse:
        all_chapters = self._repository.get_chapters(request.book_id)

        def _matches(chapter_number: str) -> bool:
            return any(
                chapter_number == n or chapter_number.startswith(n + ".")
                for n in request.chapter_numbers
            )

        matched = [ch for ch in all_chapters if _matches(ch.number)]
        for ch in matched:
            self._repository.update_chapter_include(ch.id, request.include)
            logger.info("Chapter %r (number=%r) include=%s", ch.id, ch.number, request.include)

        return SetExcludedSectionsResponse(
            book_id=request.book_id,
            updated_count=len(matched),
        )

