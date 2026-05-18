"""
Central API router — aggregates all route modules.
Import this in app/main.py and mount with settings.API_V1_STR.
"""

from fastapi import APIRouter


from app.api.routes.epub import router as epub_router
from app.api.routes.summary_jobs import router as summary_jobs_router
from app.api.routes.marp_llm import router as marp_llm_router
from app.api.routes.summarize import router as summarize_router

api_router = APIRouter()
api_router.include_router(epub_router)
api_router.include_router(summary_jobs_router)
api_router.include_router(marp_llm_router)
api_router.include_router(summarize_router)
