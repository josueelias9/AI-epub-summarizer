"""
Application-layer DTOs for EPUB use cases.

These are plain dataclasses — no framework dependency.
The API layer maps its Pydantic schemas into these before calling a use case,
and maps the returned response DTOs back to Pydantic schemas for the HTTP response.
"""
from dataclasses import dataclass, field
from typing import List, Optional


# ---------------------------------------------------------------------------
# Extract
# ---------------------------------------------------------------------------

@dataclass
class ExtractEpubRequest:
    epub_path: str
    book_key: str
    images_output_dir: Optional[str] = None


@dataclass
class ExtractEpubResponse:
    book_key: str
    total_sections: int
    total_content_chars: int
    sections_with_summaries: int


# ---------------------------------------------------------------------------
# Summarize
# ---------------------------------------------------------------------------

@dataclass
class SummarizeEpubRequest:
    book_key: str


@dataclass
class SummarizeEpubResponse:
    book_key: str
    sections_summarized: int


# ---------------------------------------------------------------------------
# Marp
# ---------------------------------------------------------------------------

@dataclass
class GenerateMarpRequest:
    book_key: str
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
# Sections
# ---------------------------------------------------------------------------

@dataclass
class SectionDTO:
    id: str
    title: str
    depth: int
    excluded: bool
    has_summary: bool


@dataclass
class ListSectionsRequest:
    book_key: str


@dataclass
class ListSectionsResponse:
    book_key: str
    sections: List[SectionDTO] = field(default_factory=list)


@dataclass
class SetExcludedSectionsRequest:
    book_key: str
    excluded_ids: List[str] = field(default_factory=list)


@dataclass
class SetExcludedSectionsResponse:
    book_key: str
    excluded_count: int
