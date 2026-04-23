# EPUB Structure Extractor — Agent Instructions

Always respond saying "Got it, Jos"

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
  core/           ← Config (settings + API_V1_STR)
  api/
    main.py       ← Central api_router — aggregates all route modules
    routes/       ← books.py, chapters.py, jobs.py, epub.py
    schemas/      ← Pydantic request/response schemas (HTTP I/O only)
  domain/         ← Pure Python dataclasses + abstract repository interfaces (NO framework imports)
  application/
    use_cases/    ← One class per operation; depend only on domain abstractions
  infrastructure/
    database/     ← SQLModel ORM models, engine, session, init_db()
    repositories/ ← Concrete SQLModel implementations of domain interfaces
    ai/           ← Ollama client (AIAgent)
    epub/         ← EPUBExtractor
    export/       ← MarpExporter
  main.py         ← Wiring: mounts api_router at settings.API_V1_STR, calls init_db()
  models.py       ← Legacy SQLModel table models (Book, Chapter, Metadata, ProcessingJob)
scripts/          ← run_api.py
tests/            ← test_db.py
```

**Dependency rule**: outer layers import inner layers, never the reverse. All imports use the `app.*` prefix.

### Key files
| File | Purpose |
|---|---|
| [`app/core/config.py`](app/core/config.py) | `Settings` class; `settings.API_V1_STR = "/api/v1"` |
| [`app/api/main.py`](app/api/main.py) | `api_router` — add new routers here |
| [`app/api/schemas/schemas.py`](app/api/schemas/schemas.py) | All Pydantic I/O schemas |
| [`app/domain/entities/book.py`](app/domain/entities/book.py) | `Book`, `Chapter`, `BookMetadata`, `ProcessingJob` |
| [`app/domain/repositories/interfaces.py`](app/domain/repositories/interfaces.py) | Abstract repository interfaces |
| [`app/application/use_cases/`](app/application/use_cases/) | `book_use_cases.py`, `chapter_use_cases.py`, `job_use_cases.py`, `epub_use_cases.py` |
| [`app/application/services/epub_processing_service.py`](app/application/services/epub_processing_service.py) | Full EPUB workflow orchestration |
| [`app/infrastructure/database/models.py`](app/infrastructure/database/models.py) | `BookORM`, `ChapterORM`, `MetadataORM`, `ProcessingJobORM` |
| [`app/infrastructure/database/session.py`](app/infrastructure/database/session.py) | `get_session()` FastAPI dependency; `init_db()` |
| [`app/infrastructure/repositories/sqlmodel_repositories.py`](app/infrastructure/repositories/sqlmodel_repositories.py) | ORM ↔ domain mapping + concrete repos |
| [`app/infrastructure/epub/epub_extractor.py`](app/infrastructure/epub/epub_extractor.py) | `EPUBExtractor` |
| [`app/infrastructure/export/marp_exporter.py`](app/infrastructure/export/marp_exporter.py) | `MarpExporter` |
| [`app/infrastructure/ai/ollama_agent.py`](app/infrastructure/ai/ollama_agent.py) | `AIAgent` — Ollama host defaults to `http://ollama:11434` |

## API Endpoints (all under `/api/v1`)
| Method | Path | Description |
|---|---|---|
| GET | `/books` | List books (pagination) |
| POST | `/books` | Create book |
| GET/DELETE | `/books/{id}` | Get / delete book |
| GET | `/books/{id}/chapters` | List chapters |
| GET | `/books/{id}/metadata` | Book metadata |
| GET | `/chapters/{id}` | Get chapter |
| GET | `/jobs` | List jobs (filter by status) |
| GET | `/jobs/{id}` | Get job |
| GET | `/stats` | DB statistics |
| GET | `/search/books` | Search books (`?q=`) |
| GET | `/search/chapters` | Search chapters (`?q=`) |
| **POST** | **`/epub/extract`** | Extract EPUB → JSON structure |
| **POST** | **`/epub/marp`** | JSON structure → Marp presentation |

## Conventions
- **ORM ↔ Domain mapping**: repositories convert `BookORM` → `Book`; never expose ORM models in use cases or routes.
- **Schemas ≠ Entities**: Pydantic schemas in `app/api/schemas/` are HTTP I/O only; use domain entities inside application logic.
- **Database migrations**: Tables created via `init_db()` on startup (`SQLModel.create_all`). No Alembic.
- **Adding a route**: create handler in `app/api/routes/`, register in [`app/api/main.py`](app/api/main.py).
- **`app/models.py`**: legacy flat SQLModel models kept for compatibility with `database.py`; prefer the ORM models in `app/infrastructure/database/models.py` for new code.

## API Reference
See [`API_README.md`](API_README.md), live Swagger at `/docs`, and [`api.http`](api.http) for ready-to-use request examples.
