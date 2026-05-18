import json
import uuid
from datetime import datetime
from typing import Optional

from sqlmodel import Session, select

from src.infrastructure.database.models import SummaryJobORM


class SummaryJobRepository:
    """Persistence helper for async summarisation job state."""

    def __init__(self, session: Session):
        self._session = session

    def create_job(self, book_id: str, chapter_ids: Optional[list[str]], chapters_total: int) -> SummaryJobORM:
        job = SummaryJobORM(
            id=str(uuid.uuid4()),
            book_id=book_id,
            status="queued",
            chapter_ids_json=json.dumps(chapter_ids) if chapter_ids else None,
            chapters_total=chapters_total,
            chapters_summarized=0,
            created_at=datetime.utcnow(),
        )
        self._session.add(job)
        self._session.commit()
        self._session.refresh(job)
        return job

    def get_job(self, job_id: str) -> Optional[SummaryJobORM]:
        return self._session.get(SummaryJobORM, job_id)

    def get_latest_for_book(self, book_id: str) -> Optional[SummaryJobORM]:
        statement = (
            select(SummaryJobORM)
            .where(SummaryJobORM.book_id == book_id)
            .order_by(SummaryJobORM.created_at.desc())
            .limit(1)
        )
        return self._session.exec(statement).first()

    def mark_processing(self, job_id: str) -> SummaryJobORM:
        job = self._require(job_id)
        job.status = "processing"
        job.started_at = datetime.utcnow()
        job.error_message = None
        self._session.commit()
        self._session.refresh(job)
        return job

    def mark_completed(self, job_id: str, chapters_summarized: int) -> SummaryJobORM:
        job = self._require(job_id)
        job.status = "completed"
        job.chapters_summarized = chapters_summarized
        job.completed_at = datetime.utcnow()
        self._session.commit()
        self._session.refresh(job)
        return job

    def mark_failed(self, job_id: str, error_message: str) -> SummaryJobORM:
        job = self._require(job_id)
        job.status = "failed"
        job.error_message = error_message
        job.completed_at = datetime.utcnow()
        self._session.commit()
        self._session.refresh(job)
        return job

    def parse_chapter_ids(self, job: SummaryJobORM) -> Optional[list[str]]:
        return json.loads(job.chapter_ids_json) if job.chapter_ids_json else None

    def _require(self, job_id: str) -> SummaryJobORM:
        job = self.get_job(job_id)
        if job is None:
            raise ValueError(f"Summary job {job_id!r} not found.")
        return job
