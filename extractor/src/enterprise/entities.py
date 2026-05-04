"""
Enterprise layer — pure domain entities.

No framework dependencies. These represent the core business concepts
as defined in the ERD.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Book:
    """Represents a book loaded from an EPUB file."""

    id: str
    name: str
    language: Optional[str] = None
    author: Optional[str] = None
    epub_path: Optional[str] = None


@dataclass
class Chapter:
    """Represents a single chapter (or sub-chapter) inside a book.

    ``chapter_id`` points to the parent chapter's id; None means root level.
    ``include`` controls whether this chapter participates in AI summarisation.
    ``number`` encodes both depth and order as a dotted string, e.g. "1", "2.3", "1.2.1".
    """

    id: str
    book_id: str
    title: str
    content: str
    number: str  # e.g. "1", "2.3", "1.2.1"
    include: bool = True
    summary: Optional[str] = None
    list_of_images: List[str] = field(default_factory=list)
    chapter_id: Optional[str] = None  # FK → parent Chapter.id
    summary_date: Optional[datetime] = None
    ai_generated: bool = False
