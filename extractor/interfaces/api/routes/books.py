"""
Books API routes.
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from typing import List

from domain.entities.book import Book
from application.use_cases.book_use_cases import (
    GetBooksUseCase,
    GetBookUseCase,
    CreateBookUseCase,
    DeleteBookUseCase,
)
from infrastructure.database.session import get_session
from infrastructure.repositories.sqlmodel_repositories import SQLModelBookRepository
from interfaces.api.schemas.schemas import BookCreate, BookResponse

router = APIRouter(prefix="/books", tags=["books"])


def _book_repo(session: Session = Depends(get_session)) -> SQLModelBookRepository:
    return SQLModelBookRepository(session)


@router.get("", response_model=List[BookResponse])
async def get_books(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    repo: SQLModelBookRepository = Depends(_book_repo),
):
    return GetBooksUseCase(repo).execute(skip=skip, limit=limit)


@router.get("/{book_id}", response_model=BookResponse)
async def get_book(
    book_id: int,
    repo: SQLModelBookRepository = Depends(_book_repo),
):
    result = GetBookUseCase(repo).execute(book_id)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")
    return result


@router.post("", response_model=BookResponse, status_code=201)
async def create_book(
    body: BookCreate,
    repo: SQLModelBookRepository = Depends(_book_repo),
):
    book = Book(
        title=body.title,
        author=body.author,
        isbn=body.isbn,
        description=body.description,
        language=body.language,
        publisher=body.publisher,
        publication_date=body.publication_date,
        file_path=body.file_path,
        file_size=body.file_size,
    )
    return CreateBookUseCase(repo).execute(book)


@router.delete("/{book_id}")
async def delete_book(
    book_id: int,
    repo: SQLModelBookRepository = Depends(_book_repo),
):
    title = DeleteBookUseCase(repo).execute(book_id)
    if title is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": f"Book '{title}' deleted successfully"}
