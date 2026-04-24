"""
Postgres implementation of BookRepositoryPort.

  Structure  → book_structures table (one row per book_key, structure stored as TEXT/JSON)
  Exclusions → book_exclusions table (one row per excluded section)
"""
import json
from datetime import datetime
from typing import Any, Dict, List, Optional

from sqlmodel import Session, select

from app.application.ports.service_ports import BookRepositoryPort
from app.infrastructure.database.models import BookStructureORM, BookExclusionORM


class PostgresBookRepository(BookRepositoryPort):
    """Stores book data in Postgres via SQLModel.

    Inject a SQLModel ``Session`` (e.g. from FastAPI's ``get_session`` dependency).
    """

    def __init__(self, session: Session):
        self._session = session

    # ------------------------------------------------------------------
    # Structure
    # ------------------------------------------------------------------

    def load_structure(self, book_key: str) -> Optional[Dict[str, Any]]:
        record = self._session.exec(
            select(BookStructureORM).where(BookStructureORM.book_key == book_key)
        ).first()
        if record is None:
            return None
        return json.loads(record.structure_json)

    def save_structure(self, book_key: str, structure: Dict[str, Any]) -> None:
        structure_json = json.dumps(structure, ensure_ascii=False)
        record = self._session.exec(
            select(BookStructureORM).where(BookStructureORM.book_key == book_key)
        ).first()
        if record:
            record.structure_json = structure_json
            record.updated_at = datetime.utcnow()
        else:
            record = BookStructureORM(book_key=book_key, structure_json=structure_json)
            self._session.add(record)
        self._session.commit()

    # ------------------------------------------------------------------
    # Exclusions
    # ------------------------------------------------------------------

    def load_exclusions(self, book_key: str) -> List[str]:
        records = self._session.exec(
            select(BookExclusionORM).where(BookExclusionORM.book_key == book_key)
        ).all()
        return [r.section_id for r in records]

    def save_exclusions(self, book_key: str, excluded_ids: List[str]) -> None:
        existing = self._session.exec(
            select(BookExclusionORM).where(BookExclusionORM.book_key == book_key)
        ).all()
        for record in existing:
            self._session.delete(record)
        for sid in excluded_ids:
            self._session.add(BookExclusionORM(book_key=book_key, section_id=sid))
        self._session.commit()
