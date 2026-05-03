"""
Centralized logging configuration for the EPUB Structure Extractor.
Call setup_logging() once at application startup.
"""

import logging
import sys

from app.core.config import settings


def setup_logging() -> None:
    """Configure root logger with a consistent format for the whole application."""
    level = logging.DEBUG if settings.DEBUG else logging.INFO

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(funcName)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Avoid duplicate handlers when Uvicorn reloads the app
    if not root_logger.handlers:
        root_logger.addHandler(handler)

    # Quiet down noisy third-party libraries
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
