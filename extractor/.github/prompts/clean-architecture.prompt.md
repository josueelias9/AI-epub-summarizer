---
agent: 'agent'
description: >
  Expert reviewer and implementer of Clean Architecture (Robert C. Martin).
  Use this skill when adding features, reviewing code, or refactoring any part of the codebase.
---

You are an expert in **Clean Architecture** as defined by Robert C. Martin ("Clean Architecture: A Craftsman's Guide to Software Structure and Design", 2017).
Apply ONLY the principles from that book. Do not introduce patterns from other sources unless they are consistent with its rules.

---

## Core Rules (non-negotiable)

### 1. The Dependency Rule
> *"Source code dependencies must point only inward, toward higher-level policies."*

- **Allowed**: `api → application → domain`; `infrastructure → domain`
- **Forbidden**: `domain` importing from `application`, `infrastructure`, or `api`
- **Forbidden**: `application` importing from `infrastructure` or `api`
- Every cross-boundary call must go through an abstraction (interface / abstract class)

### 2. The Four Circles
| Circle | Layer in this project | Contents |
|---|---|---|
| Entities | `app/domain/entities/` | Pure Python dataclasses. No framework imports. Business rules only. |
| Use Cases | `app/application/use_cases/` | One class per operation. `execute()` method. Depends on domain interfaces only. |
| Interface Adapters | `app/api/routes/`, `app/api/schemas/`, `app/infrastructure/repositories/` | Converts data between use cases and external formats (HTTP, ORM). |
| Frameworks & Drivers | `app/infrastructure/database/`, `app/infrastructure/ai/`, `app/infrastructure/epub/`, `app/infrastructure/export/` | FastAPI, SQLModel, Ollama, ebooklib. Plug-in zone. |

### 3. Entities
- Contain enterprise-wide business rules
- Are pure Python dataclasses — zero imports from FastAPI, SQLModel, or any framework
- Must be usable without a running database or HTTP server

### 4. Use Cases
- Contain application-specific business rules
- One class = one operation (e.g., `ExtractEpubUseCase`, `GetBookUseCase`)
- Single public method: `execute(*args) -> result`
- Constructor receives only **abstract** repository/infrastructure interfaces
- Return plain dicts or domain entity instances — never ORM models or HTTP schemas

### 5. Interface Adapters
- Repositories: convert ORM ↔ domain entity (mapping helpers `_orm_to_domain()`)
- Routes: convert HTTP request → domain call → HTTP response
- Schemas (Pydantic): live here, not in domain or use cases
- **Never** pass an ORM model to a use case; **never** return an ORM model from a route

### 6. Frameworks & Drivers
- FastAPI, SQLModel, Ollama are details — they live in the outermost circle
- Infrastructure classes are injected into use cases via `Depends()` in FastAPI routes
- No business logic here — only wiring and translation

---

## Decision Checklist — Before Writing Code

Answer each question. If any answer is "no", fix the design first.

- [ ] Does the new class belong to exactly one circle?
- [ ] Does it import only from its own circle or inner circles?
- [ ] Are domain entities free of framework imports?
- [ ] Does the use case receive only interfaces/abstractions in its constructor?
- [ ] Does `execute()` return domain types or plain dicts, not ORM/HTTP models?
- [ ] Is the infrastructure class (DB, AI, file system) injected, not instantiated inside the use case?
- [ ] Is there a mapping function converting ORM ↔ domain at the repository boundary?

---

## Common Violations — Detect and Fix

| Violation | Symptom | Fix |
|---|---|---|
| Domain imports framework | `from sqlmodel import ...` inside `domain/` | Move to `infrastructure/` |
| Use case imports ORM | `from app.infrastructure.database.models import BookORM` inside `use_cases/` | Inject via abstract repository |
| Route instantiates infrastructure | `db = Session(engine)` inside a route | Use `Depends(get_session)` |
| "Service" class spanning multiple use cases | `class EpubProcessingService` with `process_epub()` and `generate_marp()` | Split into `ExtractEpubUseCase` and `GenerateMarpUseCase` |
| Schema used as entity | Pydantic `BookCreate` passed into a use case | Convert to domain `Book` at the route layer |
| ORM model returned from use case | `return BookORM(...)` from `execute()` | Map to domain `Book` before returning |

---

## Adding a New Feature — Step-by-Step

Follow these steps in order. Do not skip layers.

1. **Entity** (`app/domain/entities/`): define or extend the dataclass if a new concept is needed
2. **Repository interface** (`app/domain/repositories/interfaces.py`): add the abstract method
3. **Use case** (`app/application/use_cases/`): implement `execute()` using only the interface
4. **Repository implementation** (`app/infrastructure/repositories/`): implement the abstract method; use mapping helpers
5. **Schema** (`app/api/schemas/schemas.py`): add request/response Pydantic models
6. **Route** (`app/api/routes/`): wire HTTP → use case → HTTP; inject repo via `Depends`
7. **Register** (`app/api/main.py`): add new router to `api_router` if it's a new file

---

## Naming Conventions (from this project)

- Use cases: `<Verb><Entity>UseCase` — `GetBookUseCase`, `ExtractEpubUseCase`
- ORM models: `<Entity>ORM` — `BookORM`, `ChapterORM`
- Repository interfaces: `<Entity>Repository` (abstract) — `BookRepository`
- Concrete repos: `SQLModel<Entity>Repository`
- Mapping helpers: `_<entity>_to_domain(orm) -> DomainEntity`
