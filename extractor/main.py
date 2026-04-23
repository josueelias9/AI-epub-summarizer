"""
Main FastAPI application for EPUB Structure Extractor
"""
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from database import get_db, init_db
from routes import router
from config import settings
import uvicorn

# Create FastAPI app
app = FastAPI(
    title="EPUB Structure Extractor API",
    description="API for extracting and managing EPUB book structures",
    version="1.0.0"
)

# Include routes
app.include_router(router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    init_db()

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to EPUB Structure Extractor API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    print("Starting EPUB Structure Extractor API...")
    print(f"Database: {settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")
    print(f"API will be available at: http://{settings.API_HOST}:{settings.API_PORT}")
    
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG
    )