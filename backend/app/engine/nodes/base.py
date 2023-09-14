from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from app.models.flow import Edge

from pydantic import BaseModel, validate_call

T = TypeVar("T", bound=BaseModel)


class ExecutionResult(BaseModel):
    data: dict
    next_nodes: set[str]


class BaseNode(ABC, Generic[T]):
    @validate_call
    def __init__(self, config: T, edges: list[Edge]) -> None:
        self._config = config

        edge_sources = {edge.source for edge in edges}
        if len(edge_sources) > 1:
            raise ValueError("All edges must have the same source.")
        self._edges = edges

    @abstractmethod
    def execute(self, data: dict) -> ExecutionResult:
        ...
