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


@dataclass
class Chapter:
    """Represents a single chapter (or sub-chapter) inside a book.

    ``chapter_id`` points to the parent chapter's id; None means root level.
    ``include`` controls whether this chapter participates in AI summarisation.
    """

    id: str
    book_id: str
    title: str
    content: str
    order: int
    include: bool = True
    summary: Optional[str] = None
    list_of_images: List[str] = field(default_factory=list)
    chapter_id: Optional[str] = None          # FK → parent Chapter.id
    summary_date: Optional[datetime] = None
    ai_generated: bool = False
