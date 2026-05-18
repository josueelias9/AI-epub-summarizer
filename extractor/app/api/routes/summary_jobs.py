from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep
from src.infrastructure.repositories.summary_job_repository import SummaryJobRepository
from src.infrastructure.queue.rabbitmq import RabbitMQQueue
from src.infrastructure.repositories.postgres_repository import PostgresBookRepository
from src.application.use_cases.summary_job_use_cases import EnqueueSummaryJobUseCase, GetSummaryJobStatusUseCase, GetLatestSummaryJobUseCase

router = APIRouter(prefix="/epub/summarize", tags=["summary-jobs"])

@router.post("/queue")
async def enqueue_summarize_epub(body: dict, session: SessionDep):
    """Queue AI summaries and return immediately with a job id."""
    use_case = EnqueueSummaryJobUseCase(
        repository=PostgresBookRepository(session),
        job_repository=SummaryJobRepository(session),
        queue=RabbitMQQueue(),
    )
    return use_case.execute(body)

@router.get("/jobs/{job_id}")
async def summarize_job_status(job_id: str, session: SessionDep):
    use_case = GetSummaryJobStatusUseCase(job_repository=SummaryJobRepository(session))
    return use_case.execute(job_id)

@router.get("/jobs/latest/{book_id}")
async def latest_summarize_job_status(book_id: str, session: SessionDep):
    use_case = GetLatestSummaryJobUseCase(job_repository=SummaryJobRepository(session))
    return use_case.execute(book_id)
