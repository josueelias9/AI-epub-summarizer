"""
Application-layer service ports.

These ABCs define what the application layer needs from the outside world
(AI, file parsing, export).  Infrastructure provides the concrete adapters.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


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
    ) -> None:
        ...


class StructureRepositoryPort(ABC):
    """Port for persisting and loading the hierarchical book structure extracted from an EPUB."""

    @abstractmethod
    def load(self, book_key: str) -> Optional[Dict[str, Any]]:
        """Return the stored structure, or None if not found."""
        ...

    @abstractmethod
    def save(self, book_key: str, structure: Dict[str, Any]) -> None:
        """Persist the structure, overwriting any existing entry."""
        ...
