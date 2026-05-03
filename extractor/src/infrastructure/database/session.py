"""
Database engine and session factory.
"""
import logging

from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings

logger = logging.getLogger(__name__)

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
    import src.infrastructure.database.models  # noqa: F401
    SQLModel.metadata.create_all(engine)
    logger.info("Database tables created successfully.")
