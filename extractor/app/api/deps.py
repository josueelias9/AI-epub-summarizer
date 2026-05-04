from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from src.application.use_cases.epub_use_cases import (
    CheckLLMConnectionUseCase,
    DeleteBookUseCase,
    ExtractEpubUseCase,
    GenerateMarpUseCase,
    GetSlidesUseCase,
    ListBooksUseCase,
    ListChaptersUseCase,
    SetExcludedSectionsUseCase,
    SummarizeEpubUseCase,
)
from src.infrastructure.ai.ollama_agent import AIAgent
from src.infrastructure.database.db import get_db
from src.infrastructure.epub.epub_extractor import EPUBExtractor
from src.infrastructure.export.marp_exporter import MarpExporter
from src.infrastructure.repositories.postgres_repository import PostgresBookRepository

SessionDep = Annotated[Session, Depends(get_db)]


def _extract_use_case(session: SessionDep) -> ExtractEpubUseCase:
    return ExtractEpubUseCase(
        extractor=EPUBExtractor(),
        repository=PostgresBookRepository(session),
    )


def _summarize_use_case(session: SessionDep) -> SummarizeEpubUseCase:
    return SummarizeEpubUseCase(
        ai_agent=AIAgent(),
        repository=PostgresBookRepository(session),
    )


def _marp_use_case(session: SessionDep) -> GenerateMarpUseCase:
    return GenerateMarpUseCase(
        marp_exporter=MarpExporter(),
        repository=PostgresBookRepository(session),
    )


def _llm_use_case() -> CheckLLMConnectionUseCase:
    return CheckLLMConnectionUseCase()


def _list_books_use_case(session: SessionDep) -> ListBooksUseCase:
    return ListBooksUseCase(repository=PostgresBookRepository(session))


def _list_chapters_use_case(session: SessionDep) -> ListChaptersUseCase:
    return ListChaptersUseCase(repository=PostgresBookRepository(session))


def _set_inclusion_use_case(session: SessionDep) -> SetExcludedSectionsUseCase:
    return SetExcludedSectionsUseCase(repository=PostgresBookRepository(session))


def _delete_book_use_case(session: SessionDep) -> DeleteBookUseCase:
    return DeleteBookUseCase(repository=PostgresBookRepository(session))


def _get_slides_use_case(session: SessionDep) -> GetSlidesUseCase:
    return GetSlidesUseCase(repository=PostgresBookRepository(session))
