"""
Application-layer DTOs for EPUB use cases (Clean Architecture).

Plain dataclasses — no framework dependency.
The API layer maps its Pydantic schemas into these before calling a use case,
and maps the returned response DTOs back to Pydantic schemas for the HTTP response.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


# ---------------------------------------------------------------------------
# Extract
# ---------------------------------------------------------------------------

@dataclass
class ExtractEpubRequest:
    epub_path: str
    book_name: str
    images_output_dir: Optional[str] = None
    language: Optional[str] = None
    author: Optional[str] = None


@dataclass
class ExtractEpubResponse:
    book_id: str
    total_chapters: int
    total_content_chars: int


# ---------------------------------------------------------------------------
# Summarize
# ---------------------------------------------------------------------------

@dataclass
class SummarizeEpubRequest:
    book_id: str
    chapter_ids: Optional[List[str]] = None  # None → all included chapters


@dataclass
class SummarizeEpubResponse:
    book_id: str
    chapters_summarized: int


# ---------------------------------------------------------------------------
# Marp
# ---------------------------------------------------------------------------

@dataclass
class GenerateMarpRequest:
    book_id: str
    marp_output_path: str
    title: Optional[str] = None
    include_summaries: bool = True
    include_content: bool = False
    max_depth: int = 3


@dataclass
class GenerateMarpResponse:
    marp_output_path: str


# ---------------------------------------------------------------------------
# LLM connectivity
# ---------------------------------------------------------------------------

@dataclass
class CheckLLMConnectionResponse:
    connected: bool
    host: str
    model: str


# ---------------------------------------------------------------------------
# Chapter listing
# ---------------------------------------------------------------------------

@dataclass
class ChapterDTO:
    id: str
    title: str
    number: str                   # e.g. "1", "2.3", "1.2.1"
    include: bool
    has_summary: bool
    chapter_id: Optional[str]     # parent chapter id


@dataclass
class ListChaptersRequest:
    book_id: str


@dataclass
class ListChaptersResponse:
    book_id: str
    chapters: List[ChapterDTO] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Inclusion / exclusion
# ---------------------------------------------------------------------------

@dataclass
class SetExcludedSectionsRequest:
    """Set the ``include`` flag for a list of chapters.

    Pass ``include=False`` to exclude chapters from AI summarisation,
    ``include=True`` to re-include them.
    """
    book_id: str
    chapter_ids: List[str]
    include: bool


@dataclass
class SetExcludedSectionsResponse:
    book_id: str
    updated_count: int
