"""
Pydantic schemas for request/response serialization.
These live at the interface boundary and are separate from domain entities.
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# ---- Book schemas ----

class BookCreate(BaseModel):
    title: str
    author: Optional[str] = None
    isbn: Optional[str] = None
    description: Optional[str] = None
    language: str = "en"
    publisher: Optional[str] = None
    publication_date: Optional[str] = None
    file_path: Optional[str] = None
    file_size: Optional[int] = None


class BookResponse(BaseModel):
    id: int
    title: str
    author: Optional[str] = None
    isbn: Optional[str] = None
    description: Optional[str] = None
    language: str
    publisher: Optional[str] = None
    publication_date: Optional[str] = None
    file_path: Optional[str] = None
    file_size: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    chapter_count: int = 0

    class Config:
        from_attributes = True


# ---- Chapter schemas ----

class ChapterResponse(BaseModel):
    id: int
    book_id: int
    title: str
    chapter_number: Optional[int] = None
    content: Optional[str] = None
    word_count: int = 0
    summary: Optional[str] = None
    file_name: Optional[str] = None
    order_index: int = 0
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ---- Metadata schemas ----

class MetadataResponse(BaseModel):
    id: int
    book_id: int
    key: str
    value: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ---- Job schemas ----

class JobResponse(BaseModel):
    id: int
    book_id: Optional[int] = None
    job_type: str
    status: str
    progress: int = 0
    error_message: Optional[str] = None
    result_data: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ---- EPUB processing schemas ----

class ExtractRequest(BaseModel):
    epub_path: Optional[str] = None        # defaults to INPUT_PATH/EPUB_FILE from config
    json_output: Optional[str] = None      # defaults to OUTPUT_PATH/book_with_summaries.json
    generate_summaries: bool = False


class ExtractResponse(BaseModel):
    json_output: str
    total_sections: int
    total_content_chars: int
    sections_with_summaries: int


class MarpRequest(BaseModel):
    json_path: Optional[str] = None        # defaults to OUTPUT_PATH/book_with_summaries.json
    marp_output: Optional[str] = None      # defaults to OUTPUT_PATH/book_presentation.md
    title: Optional[str] = None
    include_summaries: bool = True
    include_content: bool = False
    max_depth: int = 3


class MarpResponse(BaseModel):
    marp_output: str
