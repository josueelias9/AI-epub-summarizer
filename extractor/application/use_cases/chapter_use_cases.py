"""
Use cases for chapters, metadata, and search.
"""
from typing import List, Optional

from domain.entities.book import Chapter, BookMetadata
from domain.repositories.interfaces import (
    BookRepository,
    ChapterRepository,
    MetadataRepository,
)


class GetChaptersUseCase:
    def __init__(self, book_repo: BookRepository, chapter_repo: ChapterRepository):
        self._book_repo = book_repo
        self._chapter_repo = chapter_repo

    def execute(self, book_id: int) -> Optional[List[Chapter]]:
        if not self._book_repo.get_by_id(book_id):
            return None
        return self._chapter_repo.get_by_book(book_id)


class GetChapterUseCase:
    def __init__(self, chapter_repo: ChapterRepository):
        self._chapter_repo = chapter_repo

    def execute(self, chapter_id: int) -> Optional[Chapter]:
        return self._chapter_repo.get_by_id(chapter_id)


class SearchChaptersUseCase:
    def __init__(self, chapter_repo: ChapterRepository):
        self._chapter_repo = chapter_repo

    def execute(self, query: str, book_id: Optional[int] = None) -> List[Chapter]:
        return self._chapter_repo.search(query, book_id)


class GetMetadataUseCase:
    def __init__(self, book_repo: BookRepository, metadata_repo: MetadataRepository):
        self._book_repo = book_repo
        self._metadata_repo = metadata_repo

    def execute(self, book_id: int) -> Optional[List[BookMetadata]]:
        if not self._book_repo.get_by_id(book_id):
            return None
        return self._metadata_repo.get_by_book(book_id)
