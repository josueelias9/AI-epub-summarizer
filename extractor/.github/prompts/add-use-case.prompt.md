---
mode: agent
description: Scaffold a new use case following Clean Architecture conventions
---

Create a new use case named **${input:useCaseName}** for the entity **${input:entity:book|chapter|job}**.

Follow these steps in order:

## 1 — Domain: repository interface (if method is missing)
Add the abstract method to the relevant interface in [`app/domain/repositories/interfaces.py`](../../app/domain/repositories/interfaces.py).
- Import only from `app/domain/entities/book.py` — no framework imports.
- Use `@abstractmethod` and type annotations.

## 2 — Application: use case class
Create or extend the appropriate file in [`app/application/use_cases/`](../../app/application/use_cases/):
- Class name: `<Verb><Entity>UseCase` (e.g. `ArchiveBookUseCase`).
- Constructor receives only abstract repository types from `app.domain.repositories.interfaces`.
- `execute()` returns plain dicts or domain entity values — never ORM models.
- No `Session`, no `SQLModel`, no FastAPI imports.

## 3 — Infrastructure: repository implementation
Add the concrete method to [`app/infrastructure/repositories/sqlmodel_repositories.py`](../../app/infrastructure/repositories/sqlmodel_repositories.py):
- Use the existing `_<entity>_to_domain()` mapping helper for every returned object.
- Interact with ORM models (`BookORM`, `ChapterORM`, etc.) from `app/infrastructure/database/models.py`.

## 4 — Interface: route + schema
- Add a Pydantic response schema to [`app/api/schemas/schemas.py`](../../app/api/schemas/schemas.py) if needed.
- Add the FastAPI endpoint to the relevant router in [`app/api/routes/`](../../app/api/routes/).
- Instantiate the use case inside the route function, injecting the concrete repository via `Depends(_<entity>_repo)`.
- Raise `HTTPException(404)` when the use case returns `None`.

## Checklist
- [ ] No cross-layer imports (e.g. `app.infrastructure` not imported from `app.application`)
- [ ] New endpoint listed in [`api.http`](../../api.http) as an example request
- [ ] Route prefix follows existing pattern (`/api/v1/<entity>s`)
