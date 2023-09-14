from fastapi import APIRouter, HTTPException, status
from app.models.flow import Flow
from app.services.flow import flowService
from app.api.exceptions import HTTPError

router = APIRouter()

@router.get("/restore/{flow_id}", responses={
    status.HTTP_200_OK: {"model": Flow},
    status.HTTP_404_NOT_FOUND: {"model":HTTPError, "description":"flow not found"}
})
def restore(flow_id: str) -> Flow:
    flow = flowService.find_by_id(flow_id)
    if flow is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "flow not found")
    return flow


@router.put("/save", status_code=status.HTTP_204_NO_CONTENT)
def save(input: Flow):
    flowService.save(input)
