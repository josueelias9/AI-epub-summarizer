"""
Postgres implementation of BookRepositoryPort (Clean Architecture).

Stores BOOK and CHAPTER entities in Postgres via SQLModel.
Inject a SQLModel ``Session`` (e.g. from FastAPI's ``get_session`` dependency).
"""
import json
import logging
from datetime import datetime
from typing import List, Optional

from sqlmodel import Session, select

from src.application.ports.service_ports import BookRepositoryPort
from src.enterprise.entities import Book, Chapter
from src.infrastructure.database.models import BookORM, ChapterORM

logger = logging.getLogger(__name__)


class PostgresBookRepository(BookRepositoryPort):

    def __init__(self, session: Session):
        self._session = session

    # ------------------------------------------------------------------
    # Book
    # ------------------------------------------------------------------

    def save_book(self, book: Book) -> None:
        existing = self._session.get(BookORM, book.id)
        if existing:
            existing.name = book.name
            existing.language = book.language
            existing.author = book.author
        else:
            self._session.add(
                BookORM(id=book.id, name=book.name, language=book.language, author=book.author)
            )
        self._session.commit()
        logger.debug("Saved book %r", book.id)

    def get_book(self, book_id: str) -> Optional[Book]:
        orm = self._session.get(BookORM, book_id)
        if orm is None:
            return None
        return Book(id=orm.id, name=orm.name, language=orm.language, author=orm.author)

    # ------------------------------------------------------------------
    # Chapters
    # ------------------------------------------------------------------

    def save_chapters(self, chapters: List[Chapter]) -> None:
        for ch in chapters:
            images_json = json.dumps(ch.list_of_images, ensure_ascii=False)
            existing = self._session.get(ChapterORM, ch.id)
            if existing:
                existing.title = ch.title
                existing.content = ch.content
                existing.summary = ch.summary
                existing.list_of_images = images_json
                existing.chapter_id = ch.chapter_id
                existing.summary_date = ch.summary_date
                existing.ai_generated = ch.ai_generated
                existing.number = ch.number
                existing.include = ch.include
            else:
                self._session.add(
                    ChapterORM(
                        id=ch.id,
                        book_id=ch.book_id,
                        title=ch.title,
                        content=ch.content,
                        summary=ch.summary,
                        list_of_images=images_json,
                        chapter_id=ch.chapter_id,
                        summary_date=ch.summary_date,
                        ai_generated=ch.ai_generated,
                        number=ch.number,
                        include=ch.include,
                    )
                )
        self._session.commit()
        logger.debug("Saved %d chapters", len(chapters))

    def get_chapters(
        self, book_id: str, include_only: Optional[bool] = None
    ) -> List[Chapter]:
        query = select(ChapterORM).where(ChapterORM.book_id == book_id)
        if include_only is not None:
            query = query.where(ChapterORM.include == include_only)
        results = self._session.exec(query).all()
        return sorted(
            [self._to_entity(orm) for orm in results],
            key=lambda c: [int(x) for x in c.number.split(".")],
        )

    def get_chapter(self, chapter_id: str) -> Optional[Chapter]:
        orm = self._session.get(ChapterORM, chapter_id)
        return self._to_entity(orm) if orm else None

    def update_chapter_include(self, chapter_id: str, include: bool) -> None:
        orm = self._session.get(ChapterORM, chapter_id)
        if orm is None:
            raise ValueError(f"Chapter {chapter_id!r} not found.")
        orm.include = include
        self._session.commit()
        logger.debug("Chapter %r include=%s", chapter_id, include)

    def update_chapter_summary(
        self,
        chapter_id: str,
        summary: str,
        summary_date: datetime,
        ai_generated: bool,
    ) -> None:
        orm = self._session.get(ChapterORM, chapter_id)
        if orm is None:
            raise ValueError(f"Chapter {chapter_id!r} not found.")
        orm.summary = summary
        orm.summary_date = summary_date
        orm.ai_generated = ai_generated
        self._session.commit()
        logger.debug("Summary saved for chapter %r", chapter_id)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _to_entity(orm: ChapterORM) -> Chapter:
        images: List[str] = json.loads(orm.list_of_images) if orm.list_of_images else []
        return Chapter(
            id=orm.id,
            book_id=orm.book_id,
            title=orm.title,
            content=orm.content,
            number=orm.number,
            include=orm.include,
            summary=orm.summary,
            list_of_images=images,
            chapter_id=orm.chapter_id,
            summary_date=orm.summary_date,
            ai_generated=orm.ai_generated,
        )
