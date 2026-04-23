"""
Use case: list, get, create, and delete Books.
Depends only on domain abstractions.
"""
from typing import List, Optional

from domain.entities.book import Book
from domain.repositories.interfaces import BookRepository, ChapterRepository


class GetBooksUseCase:
    def __init__(self, book_repo: BookRepository):
        self._book_repo = book_repo

    def execute(self, skip: int = 0, limit: int = 100) -> List[dict]:
        books = self._book_repo.get_all(skip=skip, limit=limit)
        return [
            {**book.__dict__, "chapter_count": self._book_repo.chapter_count(book.id)}
            for book in books
        ]


class GetBookUseCase:
    def __init__(self, book_repo: BookRepository):
        self._book_repo = book_repo

    def execute(self, book_id: int) -> Optional[dict]:
        book = self._book_repo.get_by_id(book_id)
        if not book:
            return None
        return {**book.__dict__, "chapter_count": self._book_repo.chapter_count(book.id)}


class CreateBookUseCase:
    def __init__(self, book_repo: BookRepository):
        self._book_repo = book_repo

    def execute(self, book: Book) -> dict:
        created = self._book_repo.create(book)
        return {**created.__dict__, "chapter_count": 0}


class DeleteBookUseCase:
    def __init__(self, book_repo: BookRepository):
        self._book_repo = book_repo

    def execute(self, book_id: int) -> Optional[str]:
        book = self._book_repo.get_by_id(book_id)
        if not book:
            return None
        self._book_repo.delete(book_id)
        return book.title


class SearchBooksUseCase:
    def __init__(self, book_repo: BookRepository):
        self._book_repo = book_repo

    def execute(self, query: str) -> List[dict]:
        books = self._book_repo.search(query)
        return [
            {**book.__dict__, "chapter_count": self._book_repo.chapter_count(book.id)}
            for book in books
        ]
