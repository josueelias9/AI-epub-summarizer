"""
SQLModel models for EPUB Structure Extractor
"""
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class Book(SQLModel, table=True):
    """Model for storing book information"""
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
    file_size: Optional[int] = Field(default=None)  # in bytes
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationships
    chapters: List["Chapter"] = Relationship(back_populates="book", cascade_delete=True)
    metadata_entries: List["Metadata"] = Relationship(back_populates="book", cascade_delete=True)

class Chapter(SQLModel, table=True):
    """Model for storing chapter information"""
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
    
    # Relationships
    book: Optional[Book] = Relationship(back_populates="chapters")

class Metadata(SQLModel, table=True):
    """Model for storing additional book metadata"""
    __tablename__ = "metadata"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    book_id: int = Field(foreign_key="books.id")
    key: str = Field(max_length=100)
    value: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationships
    book: Optional[Book] = Relationship(back_populates="metadata_entries")

class ProcessingJob(SQLModel, table=True):
    """Model for tracking processing jobs"""
    __tablename__ = "processing_jobs"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    book_id: Optional[int] = Field(default=None, foreign_key="books.id")
    job_type: str = Field(max_length=50)  # extraction, summarization, etc.
    status: str = Field(default="pending", max_length=20)  # pending, processing, completed, failed
    progress: int = Field(default=0)  # 0-100
    error_message: Optional[str] = Field(default=None)
    result_data: Optional[str] = Field(default=None)  # JSON string
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = Field(default=None)