import logging

from src.infrastructure.database.session import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("Creating database tables")
    init_db()
    logger.info("Database tables ready")


if __name__ == "__main__":
    main()
