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


class UserORM(SQLModel, table=True):
    """Auth user for the frontend."""

    __tablename__ = "users"

    id: str = Field(primary_key=True, default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str = Field(unique=True, index=True)
    password: str  # bcrypt hash
