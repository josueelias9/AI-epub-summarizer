---
applyTo: "**/*test*.py,**/tests/**"
---

# Testing conventions

## Database connectivity
Run `python test_db.py` to verify PostgreSQL is reachable before running integration tests. It lists existing tables and provides troubleshooting output.

## Unit-testing use cases
Use cases depend only on abstract repository interfaces (`domain/repositories/interfaces.py`). Mock them with `unittest.mock.MagicMock` — do **not** spin up a real database:

```python
from unittest.mock import MagicMock
from application.use_cases.book_use_cases import GetBookUseCase

repo = MagicMock()
repo.get_by_id.return_value = Book(id=1, title="Test", language="en")
repo.chapter_count.return_value = 3

result = GetBookUseCase(repo).execute(book_id=1)
assert result["title"] == "Test"
assert result["chapter_count"] == 3
```

## Integration tests
- Inject a real `Session` from `infrastructure/database/session.py` with a test database URL.
- Always create and tear down test data within the test; do not rely on pre-existing rows.

## What not to test
- ORM mapping helpers (`_book_to_domain`, etc.) — they are thin and covered by integration tests.
- FastAPI route wiring — prefer testing the use case directly.

## No testing framework is currently configured
There is no `pytest.ini` or `setup.cfg`. Run tests with:
```bash
python -m pytest
```
Add `pytest` to `requirements.txt` if it is not already present.
