import json
from src.infrastructure.repositories.postgres_repository import PostgresBookRepository
from src.infrastructure.repositories.summary_job_repository import SummaryJobRepository
from src.infrastructure.queue.rabbitmq import RabbitMQQueue

class EnqueueSummaryJobUseCase:
    def __init__(self, repository, job_repository, queue):
        self.repository = repository
        self.job_repository = job_repository
        self.queue = queue

    def execute(self, body):
        book_id = body.get("book_id")
        chapter_ids = body.get("chapter_ids")
        if self.repository.get_book(book_id) is None:
            raise Exception(f"Book {book_id!r} not found.")
        if chapter_ids:
            chapters_total = len([
                ch for chapter_id in chapter_ids if (ch := self.repository.get_chapter(chapter_id)) is not None and ch.include
            ])
        else:
            chapters_total = len(self.repository.get_chapters(book_id, include_only=True))
        job = self.job_repository.create_job(
            book_id=book_id,
            chapter_ids=chapter_ids,
            chapters_total=chapters_total,
        )
        try:
            self.queue.publish({"job_id": job.id})
        except Exception as e:
            self.job_repository.mark_failed(job.id, f"Queue publish failed: {e}")
            raise Exception("Failed to enqueue summarization job.")
        return {
            "job_id": job.id,
            "book_id": job.book_id,
            "status": job.status,
            "chapters_total": job.chapters_total,
            "chapters_summarized": job.chapters_summarized,
            "error_message": job.error_message,
        }

class GetSummaryJobStatusUseCase:
    def __init__(self, job_repository):
        self.job_repository = job_repository
    def execute(self, job_id):
        job = self.job_repository.get_job(job_id)
        if job is None:
            raise Exception(f"Job {job_id!r} not found.")
        return {
            "job_id": job.id,
            "book_id": job.book_id,
            "status": job.status,
            "chapters_total": job.chapters_total,
            "chapters_summarized": job.chapters_summarized,
            "error_message": job.error_message,
        }

class GetLatestSummaryJobUseCase:
    def __init__(self, job_repository):
        self.job_repository = job_repository
    def execute(self, book_id):
        job = self.job_repository.get_latest_for_book(book_id)
        if job is None:
            raise Exception("No summary job found for this book.")
        return {
            "job_id": job.id,
            "book_id": job.book_id,
            "status": job.status,
            "chapters_total": job.chapters_total,
            "chapters_summarized": job.chapters_summarized,
            "error_message": job.error_message,
        }
