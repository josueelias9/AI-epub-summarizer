#!/usr/bin/env python3
"""
Simple script to test the FastAPI application
"""
import uvicorn
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.config import settings

if __name__ == "__main__":
    print("Starting EPUB Structure Extractor API...")
    print(f"Database: PostgreSQL at {settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")
    print(f"API will be available at: http://{settings.API_HOST}:{settings.API_PORT}")
    print(f"API Documentation at: http://{settings.API_HOST}:{settings.API_PORT}/docs")
    print(f"Alternative docs at: http://{settings.API_HOST}:{settings.API_PORT}/redoc")
    print(f"Debug mode: {settings.DEBUG}")
    print("\nPress Ctrl+C to stop the server")
    
    try:
        uvicorn.run(
            "app.main:app",
            host=settings.API_HOST,
            port=settings.API_PORT,
            reload=settings.DEBUG,
            log_level="info" if settings.DEBUG else "warning"
        )
    except KeyboardInterrupt:
        print("\nAPI server stopped.")