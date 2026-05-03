"""
Application-layer service ports (Clean Architecture).

ABCs define what the application layer needs from the outside world.
Infrastructure provides the concrete adapters.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from src.enterprise.entities import Book, Chapter

# ---------------------------------------------------------------------------
# Repository
# ---------------------------------------------------------------------------


class BookRepositoryPort(ABC):
    """Persistence port for books and chapters."""

    @abstractmethod
    def save_book(self, book: Book) -> None: ...

    @abstractmethod
    def get_book(self, book_id: str) -> Optional[Book]: ...

    @abstractmethod
    def save_chapters(self, chapters: List[Chapter]) -> None:
        """Upsert a batch of chapters."""
        ...

    @abstractmethod
    def get_chapters(
        self, book_id: str, include_only: Optional[bool] = None
    ) -> List[Chapter]:
        """Return chapters for a book, optionally filtered by the include flag."""
        ...

    @abstractmethod
    def get_chapter(self, chapter_id: str) -> Optional[Chapter]: ...

    @abstractmethod
    def update_chapter_include(self, chapter_id: str, include: bool) -> None:
        """Toggle the include flag on a single chapter."""
        ...

    @abstractmethod
    def update_chapter_summary(
        self,
        chapter_id: str,
        summary: str,
        summary_date: datetime,
        ai_generated: bool,
    ) -> None: ...

    @abstractmethod
    def list_books(self) -> List[Book]:
        """Return all books in the repository."""
        ...

    @abstractmethod
    def delete_book(self, book_id: str) -> None:
        """Delete a book and all its chapters."""
        ...


# ---------------------------------------------------------------------------
# EPUB extractor
# ---------------------------------------------------------------------------


class EpubExtractorPort(ABC):
    """Port for parsing an EPUB file into domain entities."""

    @abstractmethod
    def extract(
        self,
        epub_path: str,
        images_output_dir: Optional[str] = None,
    ) -> Tuple[Book, List[Chapter]]:
        """Parse the EPUB, generate a UUID for the book, and return Book + Chapter list."""
        ...


# ---------------------------------------------------------------------------
# AI service
# ---------------------------------------------------------------------------


class AIServicePort(ABC):
    """Port for AI text summarisation and connectivity checks."""

    @abstractmethod
    def summarize_content(self, content: str) -> str: ...

    @abstractmethod
    def test_connection(self) -> bool: ...

    @abstractmethod
    def get_connection_info(self) -> Dict[str, str]:
        """Return {'host': ..., 'model': ...} for diagnostics."""
        ...


# ---------------------------------------------------------------------------
# Marp exporter
# ---------------------------------------------------------------------------


class MarpExporterPort(ABC):
    """Port for rendering book entities as a Marp presentation."""

    @abstractmethod
    def export(
        self,
        book: Book,
        chapters: List[Chapter],
        output_path: str,
        include_summaries: bool = True,
        include_content: bool = False,
        max_depth: int = 3,
    ) -> None: ...
