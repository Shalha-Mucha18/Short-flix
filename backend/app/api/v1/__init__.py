from fastapi import APIRouter

from backend.app.api.v1.routes import shorts

api_router = APIRouter(prefix="/api/shorts")
api_router.include_router(shorts.router)

__all__ = ["api_router"]
