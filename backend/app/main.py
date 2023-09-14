from fastapi import FastAPI

from app.core.config import settings
from app.api import api_router


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_STR}/openapi.json",
)
app.include_router(api_router)