from typing import Any
from fastapi import APIRouter, Body, HTTPException, status
from app.engine.service import EngineService
from app.models.flow import Flow
from app.services.flow import flowService
from app.api.exceptions import HTTPError

router = APIRouter()

NOT_FOUND_RESPONSE = {
    status.HTTP_404_NOT_FOUND: {
        "model": HTTPError,
        "description": "flow not found",
    },
}


@router.get(
    "/restore/{flow_id}",
    responses={status.HTTP_200_OK: {"model": Flow}, **NOT_FOUND_RESPONSE},
)
def restore(flow_id: str) -> Flow:
    flow = flowService.find_by_id(flow_id)
    if flow is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "flow not found")
    return flow


@router.put("/save", status_code=status.HTTP_204_NO_CONTENT)
def save(input: Flow):
    flowService.save(input)


@router.post(
    "/execute/{flow_id}",
    responses={status.HTTP_200_OK: {"model": dict}, **NOT_FOUND_RESPONSE},
)
def execute(flow_id: str, payload: dict = Body(...)) -> Any:
    flow = restore(flow_id)
    engine = EngineService(flow)
    return engine.execute(payload)
