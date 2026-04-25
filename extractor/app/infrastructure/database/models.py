"""
SQLModel ORM models — infrastructure concern only.
These map to the database tables and are separate from domain entities.
"""
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, Text
from typing import Optional, List
from datetime import datetime


class BookORM(SQLModel, table=True):
    __tablename__ = "books"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=500)
    author: Optional[str] = Field(default=None, max_length=200)
    isbn: Optional[str] = Field(default=None, max_length=20, unique=True)
    description: Optional[str] = Field(default=None)
    language: str = Field(default="en", max_length=10)
    publisher: Optional[str] = Field(default=None, max_length=200)
    publication_date: Optional[str] = Field(default=None, max_length=50)
    file_path: Optional[str] = Field(default=None, max_length=1000)
    file_size: Optional[int] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    chapters: List["ChapterORM"] = Relationship(back_populates="book", cascade_delete=True)
    metadata_entries: List["MetadataORM"] = Relationship(back_populates="book", cascade_delete=True)


class ChapterORM(SQLModel, table=True):
    __tablename__ = "chapters"

    id: Optional[int] = Field(default=None, primary_key=True)
    book_id: int = Field(foreign_key="books.id")
    title: str = Field(max_length=500)
    chapter_number: Optional[int] = Field(default=None)
    content: Optional[str] = Field(default=None)
    word_count: int = Field(default=0)
    summary: Optional[str] = Field(default=None)
    file_name: Optional[str] = Field(default=None, max_length=200)
    order_index: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    book: Optional[BookORM] = Relationship(back_populates="chapters")


class MetadataORM(SQLModel, table=True):
    __tablename__ = "metadata"

    id: Optional[int] = Field(default=None, primary_key=True)
    book_id: int = Field(foreign_key="books.id")
    key: str = Field(max_length=100)
    value: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    book: Optional[BookORM] = Relationship(back_populates="metadata_entries")


class ProcessingJobORM(SQLModel, table=True):
    __tablename__ = "processing_jobs"

    id: Optional[int] = Field(default=None, primary_key=True)
    book_id: Optional[int] = Field(default=None, foreign_key="books.id")
    job_type: str = Field(max_length=50)
    status: str = Field(default="pending", max_length=20)
    progress: int = Field(default=0)
    error_message: Optional[str] = Field(default=None)
    result_data: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = Field(default=None)


class BookStructureORM(SQLModel, table=True):
    __tablename__ = "book_structures"

    id: Optional[int] = Field(default=None, primary_key=True)
    book_key: str = Field(max_length=1000, unique=True, index=True)
    structure_json: str = Field(sa_column=Column(Text, nullable=False))
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class BookExclusionORM(SQLModel, table=True):
    __tablename__ = "book_exclusions"

    id: Optional[int] = Field(default=None, primary_key=True)
    book_key: str = Field(max_length=1000, index=True)
    section_id: str = Field(max_length=200)
