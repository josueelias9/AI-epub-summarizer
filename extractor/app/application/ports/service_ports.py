"""
Application-layer service ports.

These ABCs define what the application layer needs from the outside world
(AI, file parsing, export).  Infrastructure provides the concrete adapters.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class AIServicePort(ABC):
    """Port for AI text summarisation and connectivity checks."""

    @abstractmethod
    def summarize_content(self, content: str) -> str:
        ...

    @abstractmethod
    def test_connection(self) -> bool:
        ...

    @abstractmethod
    def get_connection_info(self) -> Dict[str, str]:
        """Return {'host': ..., 'model': ...} for diagnostics."""
        ...


class EpubExtractorPort(ABC):
    """Port for parsing an EPUB file into a hierarchical dict structure."""

    @abstractmethod
    def extract_structure(
        self, epub_path: str, images_output_dir: Optional[str] = None
    ) -> Dict[str, Any]:
        ...


class MarpExporterPort(ABC):
    """Port for rendering a JSON book structure as a Marp presentation."""

    @abstractmethod
    def export_from_json(
        self,
        json_path: str,
        output_path: str,
        title: Optional[str] = None,
        include_summaries: bool = True,
        include_content: bool = False,
        max_depth: int = 3,
        excluded_ids: Optional[List[str]] = None,
    ) -> None:
        ...


class BookRepositoryPort(ABC):
    """Unified port for all book data: structure + excluded sections.

    Two concrete implementations exist:
      - LocalBookRepository  : JSON file (structure) + CSV file (exclusions)
      - PostgresBookRepository: Postgres tables for both
    """

    @abstractmethod
    def load_structure(self, book_key: str) -> Optional[Dict[str, Any]]:
        """Return the stored structure, or None if not found."""
        ...

    @abstractmethod
    def save_structure(self, book_key: str, structure: Dict[str, Any]) -> None:
        """Persist the structure, overwriting any existing entry."""
        ...

    @abstractmethod
    def load_exclusions(self, book_key: str) -> List[str]:
        """Return the list of excluded section IDs, or [] if none saved."""
        ...

    @abstractmethod
    def save_exclusions(self, book_key: str, excluded_ids: List[str]) -> None:
        """Persist the list of excluded section IDs, overwriting any existing entry."""
        ...
