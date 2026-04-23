"""
Main FastAPI application for EPUB Structure Extractor.
Wires together all Clean Architecture layers.
"""
from fastapi import FastAPI
from app.core.config import settings
from app.infrastructure.database.session import init_db
from app.api.main import api_router
import uvicorn

app = FastAPI(
    title="EPUB Structure Extractor API",
    description="API for extracting and managing EPUB book structures",
    version="2.0.0",
)

PREFIX = settings.API_V1_STR
app.include_router(api_router, prefix=PREFIX)


@app.on_event("startup")
async def startup_event():
    init_db()


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
    print("Starting EPUB Structure Extractor API...")
    print(f"Database: {settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")
    print(f"API will be available at: http://{settings.API_HOST}:{settings.API_PORT}")
    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
    )