"""
Chapters and metadata API routes.
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from typing import List, Optional

from app.application.use_cases.chapter_use_cases import (
    GetChaptersUseCase,
    GetChapterUseCase,
    GetMetadataUseCase,
    SearchChaptersUseCase,
)
from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.sqlmodel_repositories import (
    SQLModelBookRepository,
    SQLModelChapterRepository,
    SQLModelMetadataRepository,
)
from app.api.schemas.schemas import ChapterResponse, MetadataResponse

router = APIRouter(tags=["chapters"])


def _repos(session: Session = Depends(get_session)):
    return (
        SQLModelBookRepository(session),
        SQLModelChapterRepository(session),
        SQLModelMetadataRepository(session),
    )


@router.get("/books/{book_id}/chapters", response_model=List[ChapterResponse])
async def get_book_chapters(
    book_id: int,
    repos=Depends(_repos),
):
    book_repo, chapter_repo, _ = repos
    result = GetChaptersUseCase(book_repo, chapter_repo).execute(book_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return result


@router.get("/chapters/{chapter_id}", response_model=ChapterResponse)
async def get_chapter(
    chapter_id: int,
    repos=Depends(_repos),
):
    _, chapter_repo, _ = repos
    chapter = GetChapterUseCase(chapter_repo).execute(chapter_id)
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return chapter


@router.get("/books/{book_id}/metadata", response_model=List[MetadataResponse])
async def get_book_metadata(
    book_id: int,
    repos=Depends(_repos),
):
    book_repo, _, metadata_repo = repos
    result = GetMetadataUseCase(book_repo, metadata_repo).execute(book_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return result
