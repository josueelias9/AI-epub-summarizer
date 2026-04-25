# TODO Is this necessary?

"""
SQLModel implementations of the domain repository interfaces.
"""
from typing import List, Optional
from sqlmodel import Session, select, func

from app.domain.entities.book import Book, Chapter, BookMetadata, ProcessingJob
from app.domain.repositories.interfaces import (
    BookRepository,
    ChapterRepository,
    MetadataRepository,
    JobRepository,
)
from app.infrastructure.database.models import (
    BookORM,
    ChapterORM,
    MetadataORM,
    ProcessingJobORM,
)


# ---------------------------------------------------------------------------
# Mapping helpers
# ---------------------------------------------------------------------------

def _book_to_domain(orm: BookORM) -> Book:
    return Book(
        id=orm.id,
        title=orm.title,
        author=orm.author,
        isbn=orm.isbn,
        description=orm.description,
        language=orm.language,
        publisher=orm.publisher,
        publication_date=orm.publication_date,
        file_path=orm.file_path,
        file_size=orm.file_size,
        created_at=orm.created_at,
        updated_at=orm.updated_at,
    )


def _chapter_to_domain(orm: ChapterORM) -> Chapter:
    return Chapter(
        id=orm.id,
        book_id=orm.book_id,
        title=orm.title,
        chapter_number=orm.chapter_number,
        content=orm.content,
        word_count=orm.word_count,
        summary=orm.summary,
        file_name=orm.file_name,
        order_index=orm.order_index,
        created_at=orm.created_at,
    )


def _metadata_to_domain(orm: MetadataORM) -> BookMetadata:
    return BookMetadata(
        id=orm.id,
        book_id=orm.book_id,
        key=orm.key,
        value=orm.value,
        created_at=orm.created_at,
    )


def _job_to_domain(orm: ProcessingJobORM) -> ProcessingJob:
    return ProcessingJob(
        id=orm.id,
        book_id=orm.book_id,
        job_type=orm.job_type,
        status=orm.status,
        progress=orm.progress,
        error_message=orm.error_message,
        result_data=orm.result_data,
        created_at=orm.created_at,
        updated_at=orm.updated_at,
        completed_at=orm.completed_at,
    )


# ---------------------------------------------------------------------------
# Repository implementations
# ---------------------------------------------------------------------------

class SQLModelBookRepository(BookRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Book]:
        rows = self._session.exec(select(BookORM).offset(skip).limit(limit)).all()
        return [_book_to_domain(r) for r in rows]

    def get_by_id(self, book_id: int) -> Optional[Book]:
        row = self._session.get(BookORM, book_id)
        return _book_to_domain(row) if row else None

    def create(self, book: Book) -> Book:
        orm = BookORM(
            title=book.title,
            author=book.author,
            isbn=book.isbn,
            description=book.description,
            language=book.language,
            publisher=book.publisher,
            publication_date=book.publication_date,
            file_path=book.file_path,
            file_size=book.file_size,
        )
        self._session.add(orm)
        self._session.commit()
        self._session.refresh(orm)
        return _book_to_domain(orm)

    def delete(self, book_id: int) -> bool:
        row = self._session.get(BookORM, book_id)
        if not row:
            return False
        self._session.delete(row)
        self._session.commit()
        return True

    def search(self, query: str) -> List[Book]:
        rows = self._session.exec(
            select(BookORM).where(
                BookORM.title.contains(query)
                | BookORM.author.contains(query)
                | BookORM.description.contains(query)
            )
        ).all()
        return [_book_to_domain(r) for r in rows]

    def chapter_count(self, book_id: int) -> int:
        return self._session.exec(
            select(func.count(ChapterORM.id)).where(ChapterORM.book_id == book_id)
        ).first() or 0


class SQLModelChapterRepository(ChapterRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_book(self, book_id: int) -> List[Chapter]:
        rows = self._session.exec(
            select(ChapterORM)
            .where(ChapterORM.book_id == book_id)
            .order_by(ChapterORM.order_index)
        ).all()
        return [_chapter_to_domain(r) for r in rows]

    def get_by_id(self, chapter_id: int) -> Optional[Chapter]:
        row = self._session.get(ChapterORM, chapter_id)
        return _chapter_to_domain(row) if row else None

    def create(self, chapter: Chapter) -> Chapter:
        orm = ChapterORM(
            book_id=chapter.book_id,
            title=chapter.title,
            chapter_number=chapter.chapter_number,
            content=chapter.content,
            word_count=chapter.word_count,
            summary=chapter.summary,
            file_name=chapter.file_name,
            order_index=chapter.order_index,
        )
        self._session.add(orm)
        self._session.commit()
        self._session.refresh(orm)
        return _chapter_to_domain(orm)

    def search(self, query: str, book_id: Optional[int] = None) -> List[Chapter]:
        stmt = select(ChapterORM).where(
            ChapterORM.title.contains(query)
            | ChapterORM.content.contains(query)
            | ChapterORM.summary.contains(query)
        )
        if book_id is not None:
            stmt = stmt.where(ChapterORM.book_id == book_id)
        rows = self._session.exec(stmt).all()
        return [_chapter_to_domain(r) for r in rows]


class SQLModelMetadataRepository(MetadataRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_book(self, book_id: int) -> List[BookMetadata]:
        rows = self._session.exec(
            select(MetadataORM).where(MetadataORM.book_id == book_id)
        ).all()
        return [_metadata_to_domain(r) for r in rows]

    def create(self, metadata: BookMetadata) -> BookMetadata:
        orm = MetadataORM(book_id=metadata.book_id, key=metadata.key, value=metadata.value)
        self._session.add(orm)
        self._session.commit()
        self._session.refresh(orm)
        return _metadata_to_domain(orm)


class SQLModelJobRepository(JobRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_all(self, status: Optional[str] = None) -> List[ProcessingJob]:
        stmt = select(ProcessingJobORM).order_by(ProcessingJobORM.created_at.desc())
        if status:
            stmt = stmt.where(ProcessingJobORM.status == status)
        rows = self._session.exec(stmt).all()
        return [_job_to_domain(r) for r in rows]

    def get_by_id(self, job_id: int) -> Optional[ProcessingJob]:
        row = self._session.get(ProcessingJobORM, job_id)
        return _job_to_domain(row) if row else None

    def create(self, job: ProcessingJob) -> ProcessingJob:
        orm = ProcessingJobORM(
            book_id=job.book_id,
            job_type=job.job_type,
            status=job.status,
            progress=job.progress,
            error_message=job.error_message,
            result_data=job.result_data,
        )
        self._session.add(orm)
        self._session.commit()
        self._session.refresh(orm)
        return _job_to_domain(orm)

    def update(self, job: ProcessingJob) -> ProcessingJob:
        row = self._session.get(ProcessingJobORM, job.id)
        if not row:
            raise ValueError(f"ProcessingJob {job.id} not found")
        row.status = job.status
        row.progress = job.progress
        row.error_message = job.error_message
        row.result_data = job.result_data
        row.completed_at = job.completed_at
        self._session.add(row)
        self._session.commit()
        self._session.refresh(row)
        return _job_to_domain(row)

    def count_by_status(self) -> dict:
        rows = self._session.exec(
            select(ProcessingJobORM.status, func.count(ProcessingJobORM.id)).group_by(
                ProcessingJobORM.status
            )
        ).all()
        return {status: count for status, count in rows}
