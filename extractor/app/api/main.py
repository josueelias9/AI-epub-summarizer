"""
Central API router — aggregates all route modules.
Import this in app/main.py and mount with settings.API_V1_STR.
"""
from fastapi import APIRouter

from app.api.routes.epub import router as epub_router

api_router = APIRouter()
api_router.include_router(epub_router)
