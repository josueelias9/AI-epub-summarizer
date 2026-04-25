"""
Local (file-based) implementation of BookRepositoryPort.

  Structure  → JSON file at the path given as book_key
  Exclusions → CSV file at <book_key_without_ext>_excluded.csv
"""
import csv
import json
import os
from datetime import datetime
from typing import Any, Dict, List, Optional

from app.application.ports.service_ports import BookRepositoryPort


class LocalBookRepository(BookRepositoryPort):
    """Stores book data on the local filesystem.

    book_key is treated as a file path, e.g. ``output/book.json``.
    The exclusions CSV is stored alongside it as ``output/book_excluded.csv``.
    """

    # ------------------------------------------------------------------
    # Structure (JSON)
    # ------------------------------------------------------------------

    def load_structure(self, book_key: str) -> Optional[Dict[str, Any]]:
        if not os.path.exists(book_key):
            return None
        with open(book_key, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_structure(self, book_key: str, structure: Dict[str, Any]) -> None:
        os.makedirs(os.path.dirname(os.path.abspath(book_key)), exist_ok=True)
        with open(book_key, "w", encoding="utf-8") as f:
            json.dump(structure, f, ensure_ascii=False, indent=2)

    # ------------------------------------------------------------------
    # Exclusions (CSV)
    # ------------------------------------------------------------------

    @staticmethod
    def _csv_path(book_key: str) -> str:
        base, _ = os.path.splitext(book_key)
        return f"{base}_excluded.csv"

    def load_exclusions(self, book_key: str) -> List[str]:
        path = self._csv_path(book_key)
        if not os.path.exists(path):
            return []
        with open(path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            return [row["id"] for row in reader if row.get("id")]

    def save_exclusions(self, book_key: str, excluded_ids: List[str]) -> None:
        path = self._csv_path(book_key)
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id"])
            writer.writeheader()
            for sid in excluded_ids:
                writer.writerow({"id": sid})
