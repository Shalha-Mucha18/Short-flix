import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.v1.routes import shorts
from backend.app.core.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, version="1.0.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # On Vercel, Mangum strips /api/shorts, so no prefix needed
    # On localhost, we need the full prefix
    prefix = "" if os.getenv("VERCEL") else "/api/shorts"
    app.include_router(shorts.router, prefix=prefix)

    return app


app = create_app()
