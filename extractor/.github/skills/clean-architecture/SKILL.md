---
name: clean-architecture
description: "Clean architecture expert for this FastAPI + SQLModel project. Use when: adding a new entity, new feature, new use case, new API endpoint, new repository, refactoring to fit clean architecture, reviewing layer violations, or asking how to structure code. Enforces strict layer separation: domain → application → infrastructure → api."
argument-hint: "Describe the feature or entity you want to add (e.g., 'add a Tag entity with CRUD endpoints')"
---

# Clean Architecture Expert

## Project Layer Map

```
app/
├── domain/            # Layer 1 — pure Python, zero framework imports
│   ├── entities/      # Dataclasses: Book, Chapter, ProcessingJob ...
│   └── repositories/  # ABCs: BookRepository, ChapterRepository ...
│       └── interfaces.py
├── application/       # Layer 2 — orchestration only
│   ├── ports/         # ABCs for external services the application layer needs
│   │   └── service_ports.py  # AIServicePort, EpubExtractorPort, MarpExporterPort ...
│   └── use_cases/     # GetBooksUseCase, CreateBookUseCase ...
├── infrastructure/    # Layer 3 — framework-specific implementations
│   ├── database/
│   │   ├── models.py  # ORM models: BookORM, ChapterORM ...
│   │   └── session.py
│   ├── repositories/  # SQLModelBookRepository ...
│   │   └── sqlmodel_repositories.py
│   ├── ai/            # AIAgent implements AIServicePort
│   ├── epub/          # EPUBExtractor implements EpubExtractorPort
│   └── export/        # MarpExporter implements MarpExporterPort
└── api/               # Layer 4 — HTTP, FastAPI, Pydantic schemas
    ├── routes/        # One router file per resource
    └── schemas/       # BookCreate, BookResponse ...
```

**Dependency rule**: each layer imports ONLY from layers closer to the center.
- `api` → `application` → `domain` ✅
- `domain` → anything outside domain ❌
- `application` → `infrastructure` ❌ (depends on ABCs, not concrete classes)

### Domain interfaces vs Application ports — critical distinction

| Where | What goes there | Rule |
|---|---|---|
| `domain/repositories/interfaces.py` | `BookRepository`, `ChapterRepository` … | Contracts for **persisting domain entities** — pure domain concern |
| `application/ports/service_ports.py` | `AIServicePort`, `EpubExtractorPort` … | Contracts for **external services the use cases consume** — application concern, not domain |

**Never put service ports in the domain layer.** The domain knows nothing about AI, file parsing, or export. Those are application-level needs.

---

## Naming Conventions

| Artifact | Pattern | Example |
|---|---|---|
| Domain entity | `{Entity}` (dataclass) | `Book`, `Chapter` |
| Repository interface | `{Entity}Repository` (ABC) | `BookRepository` |
| Use case | `{Action}{Entity}UseCase` | `CreateBookUseCase` |
| ORM model | `{Entity}ORM` (SQLModel) | `BookORM` |
| Infrastructure repo | `SQLModel{Entity}Repository` | `SQLModelBookRepository` |
| Mapping helper | `_{entity}_to_domain(orm)` | `_book_to_domain` |
| Pydantic schema (input) | `{Entity}Create` | `BookCreate` |
| Pydantic schema (output) | `{Entity}Response` | `BookResponse` |
| Route file | `{entities}.py` (plural) | `books.py` |
| Private attributes | `_snake_case` | `self._book_repo` |

---

## Step-by-Step: Adding a New Feature

### Step 1 — Domain Entity (`app/domain/entities/`)

- Pure `@dataclass`, NO imports from FastAPI, SQLModel, or SQLAlchemy.
- `id` and timestamps are `Optional` (assigned by infrastructure).
- Foreign keys are plain `int` fields.

```python
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Tag:
    name: str
    id: Optional[int] = None
    created_at: Optional[datetime] = None
```

### Step 2 — Repository Interface (`app/domain/repositories/interfaces.py`)

- Extend the existing file; do NOT create a new one.
- One ABC per entity, using `@abstractmethod`.
- Standard method signatures: `get_all()`, `get_by_id()`, `create()`, `delete()`, `search()`.

```python
class TagRepository(ABC):
    @abstractmethod
    def get_all(self, skip: int = 0, limit: int = 100) -> List[Tag]: ...
    @abstractmethod
    def get_by_id(self, tag_id: int) -> Optional[Tag]: ...
    @abstractmethod
    def create(self, tag: Tag) -> Tag: ...
    @abstractmethod
    def delete(self, tag_id: int) -> bool: ...
```

### Step 2b — Service Port (`app/application/ports/service_ports.py`) — only when a use case needs an external service

- Add to the existing `service_ports.py` file; do NOT create a new one.
- Define **only the methods the use case actually calls** — keep it minimal.
- No infrastructure imports — pure ABC with `@abstractmethod`.
- Naming: `{Capability}Port` (e.g., `AIServicePort`, `EpubExtractorPort`).
- The infrastructure adapter (e.g., `AIAgent`) inherits from this port.

```python
class NotificationPort(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> None: ...
```

### Step 3 — Use Cases (`app/application/use_cases/{entity}_use_cases.py`)

- Create a **new file** per entity.
- Each use case is a **separate class** with an `.execute()` method.
- Constructor receives ONLY abstract repository interfaces — never ORM or session objects.
- No framework imports; no HTTP concepts.

```python
class GetTagsUseCase:
    def __init__(self, tag_repo: TagRepository):
        self._tag_repo = tag_repo

    def execute(self, skip: int = 0, limit: int = 100) -> List[dict]:
        return [tag.__dict__ for tag in self._tag_repo.get_all(skip=skip, limit=limit)]

class CreateTagUseCase:
    def __init__(self, tag_repo: TagRepository):
        self._tag_repo = tag_repo

    def execute(self, tag: Tag) -> dict:
        return self._tag_repo.create(tag).__dict__
```

### Step 4 — ORM Model (`app/infrastructure/database/models.py`)

- Extend the existing file.
- Use `SQLModel` with `table=True`.
- Name: `{Entity}ORM`.
- Do NOT import from `domain/`.

```python
class TagORM(SQLModel, table=True):
    __tablename__ = "tags"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
```

### Step 5 — Infrastructure Repository (`app/infrastructure/repositories/sqlmodel_repositories.py`)

- Extend the existing file.
- Add a private `_{entity}_to_domain()` mapping function before the class.
- Class inherits from the domain interface ABC.
- Constructor takes `session: Session` only.

```python
def _tag_to_domain(orm: TagORM) -> Tag:
    return Tag(id=orm.id, name=orm.name, created_at=orm.created_at)

class SQLModelTagRepository(TagRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Tag]:
        rows = self._session.exec(select(TagORM).offset(skip).limit(limit)).all()
        return [_tag_to_domain(r) for r in rows]

    def get_by_id(self, tag_id: int) -> Optional[Tag]:
        row = self._session.get(TagORM, tag_id)
        return _tag_to_domain(row) if row else None

    def create(self, tag: Tag) -> Tag:
        orm = TagORM(name=tag.name)
        self._session.add(orm)
        self._session.commit()
        self._session.refresh(orm)
        return _tag_to_domain(orm)

    def delete(self, tag_id: int) -> bool:
        row = self._session.get(TagORM, tag_id)
        if not row:
            return False
        self._session.delete(row)
        self._session.commit()
        return True
```

### Step 6 — Pydantic Schemas (`app/api/schemas/schemas.py`)

- Extend the existing file.
- `{Entity}Create`: input fields (no `id`, no timestamps).
- `{Entity}Response`: all fields the client receives.

```python
class TagCreate(BaseModel):
    name: str

class TagResponse(BaseModel):
    id: int
    name: str
    created_at: Optional[datetime]

    class Config:
        from_attributes = True
```

### Step 7 — API Route (`app/api/routes/{entities}.py`)

- Create a **new file** per resource.
- Define a local `_tag_repo()` dependency that injects `SQLModelTagRepository`.
- Routes instantiate use cases and call `.execute()` — no business logic in routes.
- Register the router in `app/api/main.py`.

```python
router = APIRouter(prefix="/tags", tags=["tags"])

def _tag_repo(session: Session = Depends(get_session)) -> SQLModelTagRepository:
    return SQLModelTagRepository(session)

@router.get("/", response_model=List[TagResponse])
def list_tags(skip: int = 0, limit: int = 100, repo: TagRepository = Depends(_tag_repo)):
    return GetTagsUseCase(repo).execute(skip=skip, limit=limit)

@router.post("/", response_model=TagResponse, status_code=201)
def create_tag(data: TagCreate, repo: TagRepository = Depends(_tag_repo)):
    return CreateTagUseCase(repo).execute(Tag(name=data.name))

@router.delete("/{tag_id}", status_code=204)
def delete_tag(tag_id: int, repo: TagRepository = Depends(_tag_repo)):
    title = DeleteTagUseCase(repo).execute(tag_id)
    if title is None:
        raise HTTPException(status_code=404, detail="Tag not found")
```

---

## Layer Violation Checklist

Before finalizing any code, verify:

- [ ] Domain entity has **no imports** from FastAPI, SQLModel, SQLAlchemy, or Pydantic.
- [ ] Use case constructor **only accepts abstract interfaces** — `domain/repositories/` for repos, `application/ports/` for external services.
- [ ] Service ports (`*Port`) live in `application/ports/`, NOT in `domain/`.
- [ ] Use case has **no HTTP concepts** (no `Request`, no `Response`, no status codes).
- [ ] ORM model (`*ORM`) is **only imported in infrastructure layer** and below.
- [ ] Routes contain **no business logic** — only call `.execute()` and map HTTP errors.
- [ ] Mapping helper `_{entity}_to_domain()` is **private** (underscore prefix).
- [ ] New entity is registered in `app/domain/entities/__init__.py` (if applicable).
- [ ] New route router is registered in `app/api/main.py`.

---

## Testing Rules

See [testing.instructions.md](../../instructions/testing.instructions.md) for full testing conventions.

**Quick reference:**
- **Use cases**: mock the repository with `unittest.mock.MagicMock` — no real DB.
- **Integration tests**: inject a real `Session` with a test DB URL; create and tear down data per test.
- Do **not** test `_{entity}_to_domain()` helpers directly — covered by integration tests.
- Do **not** test FastAPI route wiring — test the use case directly.

---

## Anti-patterns to Reject

| Anti-pattern | Why it breaks clean architecture |
|---|---|
| `from sqlmodel import ...` inside `domain/` or `application/` | Domain must be framework-free |
| Service port (`AIServicePort`, `EpubExtractorPort` …) defined in `domain/` | Domain has no concept of AI or file I/O — those are application-layer concerns |
| Business logic in route handlers | Routes are HTTP adapters, not orchestrators |
| Use case directly using `Session` | Bypasses repository abstraction |
| ORM model exposed in API response | Leaks infrastructure details to the client |
| `*ORM` class imported in `application/` | Application must not know about the ORM |
| Skipping the mapping helper | Coupling ORM to domain entity |
| Multiple entities in one use case file | Violates single responsibility |
