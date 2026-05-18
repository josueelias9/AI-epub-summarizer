"""
Main FastAPI application for EPUB Structure Extractor.
Wires together all Clean Architecture layers.

DB initialisation is handled by scripts/prestart.sh before the server starts.
"""

import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.core.config import settings
from app.core.logging_config import setup_logging
from app.api.main import api_router
import uvicorn

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="EPUB Structure Extractor API",
    description="API for extracting and managing EPUB book structures",
    version="2.0.0",
)

# CORS — allow the Next.js frontend
# TODO: "http://localhost:3000" Should be passed as env variable
_allowed_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PREFIX = settings.API_V1_STR
app.include_router(api_router, prefix=PREFIX)

# Serve extracted images and other output files as static assets
_output_dir = "/app/output"
os.makedirs(_output_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=_output_dir), name="static")


@app.get("/")
async def root():
    return {
        "message": "Welcome to EPUB Structure Extractor API",
        "version": "2.0.0",
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    logger.info("Starting EPUB Structure Extractor API...")
    logger.info(
        "Database: %s:%s/%s", settings.DB_HOST, settings.DB_PORT, settings.DB_NAME
    )
    logger.info(
        "API will be available at: http://%s:%s", settings.API_HOST, settings.API_PORT
    )
    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
    )
