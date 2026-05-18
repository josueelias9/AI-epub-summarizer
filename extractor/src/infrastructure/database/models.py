"""
SQLModel ORM models — infrastructure concern only.

These map directly to the ERD tables (BOOK and CHAPTER) and are kept
separate from the enterprise entities.
"""

import uuid
from datetime import datetime
from typing import List, Optional

from sqlalchemy import Column, Text
from sqlmodel import Field, Relationship, SQLModel

# ========================= Database models (ERD tables) =========================


class BookORM(SQLModel, table=True):
    """Persistent representation of a Book (ERD: BOOK)."""

    __tablename__ = "book"

    id: str = Field(primary_key=True)
    name: str
    language: Optional[str] = None
    author: Optional[str] = None
    epub_path: Optional[str] = Field(default=None)

    chapters: List["ChapterORM"] = Relationship(back_populates="book")


class ChapterORM(SQLModel, table=True):
    """Persistent representation of a Chapter (ERD: CHAPTER).

    ``chapter_id`` is a self-referencing FK to ``chapter.id`` (parent chapter).
    ``include`` controls whether the chapter participates in AI summarisation.
    """

    __tablename__ = "chapter"

    id: str = Field(primary_key=True)
    book_id: str = Field(foreign_key="book.id", index=True)
    title: str
    content: str = Field(sa_column=Column(Text, nullable=False))
    summary: Optional[str] = Field(default=None, sa_column=Column(Text))
    list_of_images: Optional[str] = Field(default=None)  # JSON-encoded list
    chapter_id: Optional[str] = Field(default=None, foreign_key="chapter.id")
    summary_date: Optional[datetime] = None
    ai_generated: bool = Field(default=False)
    number: str  # e.g. "1", "2.3", "1.2.1"
    include: bool = Field(default=True)

    book: Optional[BookORM] = Relationship(back_populates="chapters")


class SummaryJobORM(SQLModel, table=True):
    """Tracks async summarisation jobs processed by the worker."""

    __tablename__ = "summary_job"

    id: str = Field(primary_key=True)
    book_id: str = Field(foreign_key="book.id", index=True)
    status: str = Field(index=True)  # queued | processing | completed | failed
    chapter_ids_json: Optional[str] = Field(default=None)
    chapters_total: int = Field(default=0)
    chapters_summarized: int = Field(default=0)
    error_message: Optional[str] = Field(default=None, sa_column=Column(Text))
    created_at: datetime = Field(default_factory=datetime.utcnow)
    started_at: Optional[datetime] = Field(default=None)
    completed_at: Optional[datetime] = Field(default=None)


class UserORM(SQLModel, table=True):
    """Auth user for the frontend."""

    __tablename__ = "users"

    id: str = Field(primary_key=True, default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str = Field(unique=True, index=True)
    password: str  # bcrypt hash



# ========================= Pydantic schemas (migrated from schemas.py) =========================

from pydantic import BaseModel

from typing import Optional

class ExtractRequest(BaseModel):
    epub_path: str
    book_name: str
    images_output_dir: Optional[str] = None
    language: Optional[str] = None
    author: Optional[str] = None

class ExtractResponse(BaseModel):
    book_id: str
    total_chapters: int
    total_content_chars: int

class SummarizeRequest(BaseModel):
    book_id: str
    chapter_ids: Optional[list[str]] = None  # None → all included chapters

class SummarizeResponse(BaseModel):
    book_id: str
    chapters_summarized: int

class MarpRequest(BaseModel):
    book_id: str
    marp_output: str
    title: Optional[str] = None
    include_summaries: bool = True
    include_content: bool = False
    max_depth: int = 3

class MarpResponse(BaseModel):
    marp_output: str

class LLMStatusResponse(BaseModel):
    connected: bool
    host: str
    model: str

class ChapterInfo(BaseModel):
    id: str
    title: str
    number: str
    include: bool
    has_summary: bool
    chapter_id: Optional[str]

class ChaptersListResponse(BaseModel):
    book_id: str
    total: int
    chapters: list[ChapterInfo]

class SetInclusionRequest(BaseModel):
    book_id: str
    chapter_numbers: list[str]
    include: bool

class SetInclusionResponse(BaseModel):
    book_id: str
    updated_count: int

class BookInfo(BaseModel):
    id: str
    name: str
    language: Optional[str] = None
    author: Optional[str] = None

class BooksListResponse(BaseModel):
    total: int
    books: list[BookInfo]

class UploadEpubResponse(BaseModel):
    book_id: str
    book_name: str
    total_chapters: int

class DeleteBookResponse(BaseModel):
    book_id: str
    success: bool

class SlideInfo(BaseModel):
    chapter_id: str
    title: str
    number: str
    summary: Optional[str] = None
    content: str
    images: list[str]
    depth: int

class SlidesResponse(BaseModel):
    book_id: str
    book_name: str
    slides: list[SlideInfo]

