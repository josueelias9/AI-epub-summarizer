"""
Local (file-based) implementation of BookRepositoryPort.

Storage layout (all relative to ``base_dir``, default "output/"):
  output/<book_id>/book.json        — Book metadata
  output/<book_id>/chapters.json    — List of serialised Chapter objects
"""
import json
import logging
import os
from datetime import datetime
from typing import List, Optional

from src.application.ports.service_ports import BookRepositoryPort
from src.enterprise.entities import Book, Chapter

logger = logging.getLogger(__name__)

_DT_FMT = "%Y-%m-%dT%H:%M:%S"


class LocalBookRepository(BookRepositoryPort):
    """Stores book data on the local filesystem as JSON files.

    ``base_dir`` is the root folder; each book lives in ``<base_dir>/<book_id>/``.
    """

    def __init__(self, base_dir: str = "output"):
        self._base = base_dir

    def _book_dir(self, book_id: str) -> str:
        return os.path.join(self._base, book_id)

    def _book_path(self, book_id: str) -> str:
        return os.path.join(self._book_dir(book_id), "book.json")

    def _chapters_path(self, book_id: str) -> str:
        return os.path.join(self._book_dir(book_id), "chapters.json")

    # ------------------------------------------------------------------
    # Book
    # ------------------------------------------------------------------

    def save_book(self, book: Book) -> None:
        os.makedirs(self._book_dir(book.id), exist_ok=True)
        data = {"id": book.id, "name": book.name, "language": book.language, "author": book.author}
        with open(self._book_path(book.id), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.debug("Saved book %r to %s", book.id, self._book_path(book.id))

    def get_book(self, book_id: str) -> Optional[Book]:
        path = self._book_path(book_id)
        if not os.path.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return Book(id=data["id"], name=data["name"], language=data.get("language"), author=data.get("author"))

    # ------------------------------------------------------------------
    # Chapters
    # ------------------------------------------------------------------

    def save_chapters(self, chapters: List[Chapter]) -> None:
        if not chapters:
            return
        book_id = chapters[0].book_id
        os.makedirs(self._book_dir(book_id), exist_ok=True)

        # Load existing chapters so we don't lose summaries on re-extract
        existing = {ch.id: ch for ch in self._load_chapters_raw(book_id)}
        for ch in chapters:
            if ch.id in existing:
                # Preserve previously generated summary
                old = existing[ch.id]
                ch.summary = ch.summary or old.summary
                ch.summary_date = ch.summary_date or old.summary_date
                ch.ai_generated = ch.ai_generated or old.ai_generated
                ch.include = old.include  # preserve manual include flag
            existing[ch.id] = ch

        ordered = sorted(existing.values(), key=lambda c: c.order)
        with open(self._chapters_path(book_id), "w", encoding="utf-8") as f:
            json.dump([self._ch_to_dict(c) for c in ordered], f, ensure_ascii=False, indent=2)
        logger.debug("Saved %d chapters for book %r", len(ordered), book_id)

    def get_chapters(self, book_id: str, include_only: Optional[bool] = None) -> List[Chapter]:
        chapters = self._load_chapters_raw(book_id)
        if include_only is not None:
            chapters = [ch for ch in chapters if ch.include == include_only]
        return sorted(chapters, key=lambda c: c.order)

    def get_chapter(self, chapter_id: str) -> Optional[Chapter]:
        # chapter_id format: "<book_id>/<section_id>" — but we stored plain section ids.
        # We must search across all books; in practice book_id is embedded in the id
        # as the caller uses book_id-prefixed lookups. Here we do a simple scan.
        for entry in os.scandir(self._base):
            if not entry.is_dir():
                continue
            for ch in self._load_chapters_raw(entry.name):
                if ch.id == chapter_id:
                    return ch
        return None

    def update_chapter_include(self, chapter_id: str, include: bool) -> None:
        self._patch_chapter(chapter_id, include=include)

    def update_chapter_summary(
        self,
        chapter_id: str,
        summary: str,
        summary_date: datetime,
        ai_generated: bool,
    ) -> None:
        self._patch_chapter(
            chapter_id,
            summary=summary,
            summary_date=summary_date,
            ai_generated=ai_generated,
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _load_chapters_raw(self, book_id: str) -> List[Chapter]:
        path = self._chapters_path(book_id)
        if not os.path.exists(path):
            return []
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [self._dict_to_ch(d) for d in data]

    def _patch_chapter(self, chapter_id: str, **kwargs) -> None:
        for entry in os.scandir(self._base):
            if not entry.is_dir():
                continue
            chapters = self._load_chapters_raw(entry.name)
            for ch in chapters:
                if ch.id == chapter_id:
                    for k, v in kwargs.items():
                        setattr(ch, k, v)
                    with open(self._chapters_path(entry.name), "w", encoding="utf-8") as f:
                        json.dump([self._ch_to_dict(c) for c in chapters], f, ensure_ascii=False, indent=2)
                    return
        raise ValueError(f"Chapter {chapter_id!r} not found in local repository.")

    @staticmethod
    def _ch_to_dict(ch: Chapter) -> dict:
        return {
            "id": ch.id,
            "book_id": ch.book_id,
            "title": ch.title,
            "content": ch.content,
            "order": ch.order,
            "include": ch.include,
            "summary": ch.summary,
            "list_of_images": ch.list_of_images,
            "chapter_id": ch.chapter_id,
            "summary_date": ch.summary_date.strftime(_DT_FMT) if ch.summary_date else None,
            "ai_generated": ch.ai_generated,
        }

    @staticmethod
    def _dict_to_ch(d: dict) -> Chapter:
        sd = d.get("summary_date")
        return Chapter(
            id=d["id"],
            book_id=d["book_id"],
            title=d["title"],
            content=d.get("content", ""),
            order=d.get("order", 0),
            include=d.get("include", True),
            summary=d.get("summary"),
            list_of_images=d.get("list_of_images", []),
            chapter_id=d.get("chapter_id"),
            summary_date=datetime.strptime(sd, _DT_FMT) if sd else None,
            ai_generated=d.get("ai_generated", False),
        )
