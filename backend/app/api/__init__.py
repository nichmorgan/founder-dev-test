from fastapi import APIRouter
from app.api.endpoints import flow

api_router = APIRouter()
api_router.include_router(flow.router, prefix="/flow", tags=["flow"])
