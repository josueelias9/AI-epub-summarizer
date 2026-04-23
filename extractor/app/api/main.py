"""
Central API router — aggregates all route modules.
Import this in app/main.py and mount with settings.API_V1_STR.
"""
from fastapi import APIRouter

from app.api.routes.books import router as books_router
from app.api.routes.chapters import router as chapters_router
from app.api.routes.jobs import router as jobs_router

api_router = APIRouter()
api_router.include_router(books_router)
api_router.include_router(chapters_router)
api_router.include_router(jobs_router)
