from fastapi import FastAPI

from app.core.config import settings
from app.api import api_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_STR}/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
