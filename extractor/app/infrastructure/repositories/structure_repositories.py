"""
Concrete adapters for StructureRepositoryPort.

  JsonFileStructureRepository  — stores the structure as a JSON file on disk.
  PostgresStructureRepository  — stores the structure as a TEXT column in Postgres.
"""
import json
import os
from datetime import datetime
from typing import Any, Dict, Optional

from sqlmodel import Session, select

from app.application.ports.service_ports import StructureRepositoryPort
from app.infrastructure.database.models import BookStructureORM


class JsonFileStructureRepository(StructureRepositoryPort):
    """Persists the book structure as a JSON file; book_key is the file path."""

    def load(self, book_key: str) -> Optional[Dict[str, Any]]:
        if not os.path.exists(book_key):
            return None
        with open(book_key, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, book_key: str, structure: Dict[str, Any]) -> None:
        os.makedirs(os.path.dirname(os.path.abspath(book_key)), exist_ok=True)
        with open(book_key, "w", encoding="utf-8") as f:
            json.dump(structure, f, ensure_ascii=False, indent=2)


class PostgresStructureRepository(StructureRepositoryPort):
    """Persists the book structure in the book_structures table; book_key is a unique string."""

    def __init__(self, session: Session):
        self._session = session

    def load(self, book_key: str) -> Optional[Dict[str, Any]]:
        record = self._session.exec(
            select(BookStructureORM).where(BookStructureORM.book_key == book_key)
        ).first()
        if record is None:
            return None
        return json.loads(record.structure_json)

    def save(self, book_key: str, structure: Dict[str, Any]) -> None:
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
