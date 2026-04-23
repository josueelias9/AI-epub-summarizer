"""
Domain entities - pure Python dataclasses with no framework dependencies.
These represent the core business objects of the application.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Book:
    title: str
    id: Optional[int] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    description: Optional[str] = None
    language: str = "en"
    publisher: Optional[str] = None
    publication_date: Optional[str] = None
    file_path: Optional[str] = None
    file_size: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class Chapter:
    book_id: int
    title: str
    id: Optional[int] = None
    chapter_number: Optional[int] = None
    content: Optional[str] = None
    word_count: int = 0
    summary: Optional[str] = None
    file_name: Optional[str] = None
    order_index: int = 0
    created_at: Optional[datetime] = None


@dataclass
class BookMetadata:
    book_id: int
    key: str
    id: Optional[int] = None
    value: Optional[str] = None
    created_at: Optional[datetime] = None


@dataclass
class ProcessingJob:
    job_type: str
    id: Optional[int] = None
    book_id: Optional[int] = None
    status: str = "pending"
    progress: int = 0
    error_message: Optional[str] = None
    result_data: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
