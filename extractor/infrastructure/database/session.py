"""
Database engine and session factory.
"""
from sqlmodel import SQLModel, create_engine, Session
from config import settings

engine = create_engine(
    settings.database_url,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=300,
)


def get_session() -> Session:
    """Yield a database session (FastAPI dependency)."""
    with Session(engine) as session:
        yield session


def init_db() -> None:
    """Create all tables."""
    # Import ORM models so SQLModel registers them before create_all
    import infrastructure.database.models  # noqa: F401
    SQLModel.metadata.create_all(engine)
    print("Database tables created successfully.")
