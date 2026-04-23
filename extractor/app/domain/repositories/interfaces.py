"""
Abstract repository interfaces for the domain layer.
Following the Dependency Inversion Principle - high-level modules depend on abstractions.
"""
from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.book import Book, Chapter, BookMetadata, ProcessingJob


class BookRepository(ABC):
    @abstractmethod
    def get_all(self, skip: int = 0, limit: int = 100) -> List[Book]:
        ...

    @abstractmethod
    def get_by_id(self, book_id: int) -> Optional[Book]:
        ...

    @abstractmethod
    def create(self, book: Book) -> Book:
        ...

    @abstractmethod
    def delete(self, book_id: int) -> bool:
        ...

    @abstractmethod
    def search(self, query: str) -> List[Book]:
        ...

    @abstractmethod
    def chapter_count(self, book_id: int) -> int:
        ...


class ChapterRepository(ABC):
    @abstractmethod
    def get_by_book(self, book_id: int) -> List[Chapter]:
        ...

    @abstractmethod
    def get_by_id(self, chapter_id: int) -> Optional[Chapter]:
        ...

    @abstractmethod
    def create(self, chapter: Chapter) -> Chapter:
        ...

    @abstractmethod
    def search(self, query: str, book_id: Optional[int] = None) -> List[Chapter]:
        ...


class MetadataRepository(ABC):
    @abstractmethod
    def get_by_book(self, book_id: int) -> List[BookMetadata]:
        ...

    @abstractmethod
    def create(self, metadata: BookMetadata) -> BookMetadata:
        ...


class JobRepository(ABC):
    @abstractmethod
    def get_all(self, status: Optional[str] = None) -> List[ProcessingJob]:
        ...

    @abstractmethod
    def get_by_id(self, job_id: int) -> Optional[ProcessingJob]:
        ...

    @abstractmethod
    def create(self, job: ProcessingJob) -> ProcessingJob:
        ...

    @abstractmethod
    def update(self, job: ProcessingJob) -> ProcessingJob:
        ...

    @abstractmethod
    def count_by_status(self) -> dict:
        ...
