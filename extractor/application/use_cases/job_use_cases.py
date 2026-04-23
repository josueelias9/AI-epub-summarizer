"""
Use cases for processing jobs and statistics.
"""
from typing import List, Optional

from domain.entities.book import ProcessingJob
from domain.repositories.interfaces import BookRepository, ChapterRepository, JobRepository
from infrastructure.database.models import ProcessingJobORM


class GetJobsUseCase:
    def __init__(self, job_repo: JobRepository):
        self._job_repo = job_repo

    def execute(self, status: Optional[str] = None) -> List[ProcessingJob]:
        return self._job_repo.get_all(status=status)


class GetJobUseCase:
    def __init__(self, job_repo: JobRepository):
        self._job_repo = job_repo

    def execute(self, job_id: int) -> Optional[ProcessingJob]:
        return self._job_repo.get_by_id(job_id)


class GetStatsUseCase:
    def __init__(
        self,
        book_repo: BookRepository,
        chapter_repo: ChapterRepository,
        job_repo: JobRepository,
    ):
        self._book_repo = book_repo
        self._chapter_repo = chapter_repo
        self._job_repo = job_repo

    def execute(self) -> dict:
        books = self._book_repo.get_all(limit=100000)
        chapters = []
        total_words = 0
        for book in books:
            book_chapters = self._chapter_repo.get_by_book(book.id)
            chapters.extend(book_chapters)
            total_words += sum(c.word_count for c in book_chapters)

        return {
            "total_books": len(books),
            "total_chapters": len(chapters),
            "total_processing_jobs": len(self._job_repo.get_all()),
            "jobs_by_status": self._job_repo.count_by_status(),
            "total_words": total_words,
        }
