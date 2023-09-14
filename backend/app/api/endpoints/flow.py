from fastapi import APIRouter, status
from app.models.flow import Flow
from app.services.flow import flowService

router = APIRouter()


@router.put("/save", status_code=status.HTTP_204_NO_CONTENT)
def save(input: Flow):
    flowService.save(input)
