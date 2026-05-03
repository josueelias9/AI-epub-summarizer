"""
Pydantic schemas for request/response serialization.
These live at the interface boundary and are separate from domain entities.
"""
from pydantic import BaseModel
from typing import Optional# ---- EPUB processing schemas ----

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


# ---- Chapter listing / inclusion schemas ----

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


# ---- Book listing / upload / delete ----

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


# ---- Slides ----

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
