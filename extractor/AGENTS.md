# EPUB Structure Extractor — Agent Instructions

## Project Overview
FastAPI + PostgreSQL service that extracts, stores, and serves EPUB book structures with AI-powered summarization via Ollama. Clean Architecture with four explicit layers.

## Running the App
```bash
# Install dependencies
pip install -r requirements.txt

# Start API (reads env vars from environment)
python scripts/run_api.py
# or: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Verify database connectivity
python tests/test_db.py
```

## Required Environment Variables
| Variable | Purpose |
|---|---|
| `DB_HOST`, `DB_PORT` | PostgreSQL host and port |
| `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` | DB credentials |
| `API_HOST`, `API_PORT` | Uvicorn bind address |
| `DEBUG` | `true`/`false` |
| `INPUT_PATH`, `OUTPUT_PATH`, `EPUB_FILE` | EPUB processing paths |

All settings are loaded in [`app/core/config.py`](app/core/config.py) via `os.getenv()` — no `.env` file loader; export variables before running.

## Architecture: Clean Architecture Layers

```
app/
  core/          ← Config and core FastAPI setup
  api/
    routes/      ← FastAPI route handlers (books, chapters, jobs)
    schemas/     ← Pydantic request/response schemas (HTTP I/O only)
  domain/        ← Pure Python dataclasses + abstract repository interfaces (NO framework imports)
  application/   ← Use cases; depend only on domain abstractions
  infrastructure/← SQLModel ORM, PostgreSQL, Ollama client, epub/export utilities
  main.py        ← Wiring only: registers routers, calls init_db()
scripts/         ← Runnable scripts (run_api.py)
tests/           ← Test files (test_db.py)
```

**Dependency rule**: outer layers import inner layers, never the reverse.

### Key files by layer
- **Config**: [`app/core/config.py`](app/core/config.py)
- **Domain entities**: [`app/domain/entities/book.py`](app/domain/entities/book.py) — `Book`, `Chapter`, `BookMetadata`, `ProcessingJob`
- **Repository interfaces**: [`app/domain/repositories/interfaces.py`](app/domain/repositories/interfaces.py)
- **Use cases**: [`app/application/use_cases/`](app/application/use_cases/)
- **ORM models**: [`app/infrastructure/database/models.py`](app/infrastructure/database/models.py) — `BookORM`, `ChapterORM`, `MetadataORM`, `ProcessingJobORM`
- **DB session / dependency**: [`app/infrastructure/database/session.py`](app/infrastructure/database/session.py) — use `get_session()` as FastAPI dependency
- **Concrete repositories**: [`app/infrastructure/repositories/sqlmodel_repositories.py`](app/infrastructure/repositories/sqlmodel_repositories.py)
- **Routes**: [`app/api/routes/`](app/api/routes/) — all mounted under `/api/v1`
- **Schemas**: [`app/api/schemas/schemas.py`](app/api/schemas/schemas.py)

## Conventions
- **ORM ↔ Domain mapping**: infrastructure repositories convert `BookORM` → `Book` (domain); never expose ORM models in use cases or routes.
- **Schemas ≠ Entities**: Pydantic schemas in `interfaces/` are for HTTP I/O only; use domain entities inside application logic.
- **Database migrations**: Tables are created via `init_db()` on startup (SQLModel `create_all`). No Alembic migrations currently.
- **AI summarization**: [`app/infrastructure/ai/ollama_agent.py`](app/infrastructure/ai/ollama_agent.py) — Ollama host defaults to `http://ollama:11434`.
- **EPUB extraction**: [`app/infrastructure/epub/epub_extractor.py`](app/infrastructure/epub/epub_extractor.py)
- **Marp export**: [`app/infrastructure/export/marp_exporter.py`](app/infrastructure/export/marp_exporter.py)

## ⚠ Legacy Code — `src/`
The [`src/`](src/) directory is **deprecated**. It contains the original monolithic scripts (`extractor.py`, `ia_agent.py`, `marp_exporter.py`, `mediator.py`). All new work goes in the layered structure above. Do not import from `src/` in new code.

## API Reference
See [`API_README.md`](API_README.md) and the live Swagger docs at `/docs` when the server is running. The [`api.http`](api.http) file has ready-to-use HTTP request examples.
