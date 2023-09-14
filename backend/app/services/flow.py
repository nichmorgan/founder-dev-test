from app.models.flow import Flow
from app.db import session


class FlowService:
    def __init__(self, repository=session.flow_collection) -> None:
        self._repository = repository

    def save(self, flow: Flow) -> None:
        self._repository.replace_one(
            filter={"id": flow.id},
            replacement=flow.model_dump(),
            upsert=True,
        )


flowService = FlowService()
