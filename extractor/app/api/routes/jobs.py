"""
Jobs, stats, and search API routes.
"""
import logging
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from typing import List, Optional

from app.application.use_cases.job_use_cases import GetJobsUseCase, GetJobUseCase, GetStatsUseCase
from app.application.use_cases.book_use_cases import SearchBooksUseCase
from app.application.use_cases.chapter_use_cases import SearchChaptersUseCase
from app.infrastructure.database.session import get_session
from app.infrastructure.repositories.sqlmodel_repositories import (
    SQLModelBookRepository,
    SQLModelChapterRepository,
    SQLModelJobRepository,
)
from app.api.schemas.schemas import BookResponse, ChapterResponse, JobResponse

logger = logging.getLogger(__name__)

router = APIRouter(tags=["jobs"])


def _all_repos(session: Session = Depends(get_session)):
    return (
        SQLModelBookRepository(session),
        SQLModelChapterRepository(session),
        SQLModelJobRepository(session),
    )


@router.get("/jobs", response_model=List[JobResponse])
async def get_jobs(
    status: Optional[str] = Query(None),
    repos=Depends(_all_repos),
):
    _, _, job_repo = repos
    return GetJobsUseCase(job_repo).execute(status=status)


@router.get("/jobs/{job_id}", response_model=JobResponse)
async def get_job(
    job_id: int,
    repos=Depends(_all_repos),
):
    _, _, job_repo = repos
    job = GetJobUseCase(job_repo).execute(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Processing job not found")
    return job


@router.get("/stats")
async def get_stats(repos=Depends(_all_repos)):
    book_repo, chapter_repo, job_repo = repos
    return GetStatsUseCase(book_repo, chapter_repo, job_repo).execute()


@router.get("/search/books", response_model=List[BookResponse])
async def search_books(
    q: str = Query(..., min_length=1),
    repos=Depends(_all_repos),
):
    book_repo, _, _ = repos
    return SearchBooksUseCase(book_repo).execute(q)


@router.get("/search/chapters", response_model=List[ChapterResponse])
async def search_chapters(
    q: str = Query(..., min_length=1),
    book_id: Optional[int] = Query(None),
    repos=Depends(_all_repos),
):
    _, chapter_repo, _ = repos
    return SearchChaptersUseCase(chapter_repo).execute(q, book_id)
