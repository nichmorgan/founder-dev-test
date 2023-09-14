from fastapi import APIRouter, status
from app.models.flow import Flow
from app.services.flow import flowService

router = APIRouter()


@router.get("/restore/{flow_id}", status_code=status.HTTP_200_OK)
def restore(flow_id: str) -> Flow:
    return flowService.find_by_id(flow_id)


@router.put("/save", status_code=status.HTTP_204_NO_CONTENT)
def save(input: Flow):
    flowService.save(input)
