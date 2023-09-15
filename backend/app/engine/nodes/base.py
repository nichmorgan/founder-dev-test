from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from app.models.flow import Edge

from pydantic import BaseModel, field_validator, validate_call

T = TypeVar("T", bound=BaseModel)


class ExecutionResult(BaseModel):
    data: dict
    next_nodes: set[str]


class NodeConfig(BaseModel, Generic[T]):
    config: T
    edges: list[Edge]

    @field_validator("edges")
    @classmethod
    def validate_edges(cls, edges: list[Edge]) -> list[Edge]:
        edge_sources = {edge.source for edge in edges}
        if len(edge_sources) > 1:
            raise ValueError("All edges must have the same source.")
        return edges


class BaseNode(ABC, Generic[T]):
    @validate_call
    def __init__(self, params: NodeConfig[T]) -> None:
        self._config = params.config
        self._edges = params.edges

    @abstractmethod
    def execute(self, data: dict) -> ExecutionResult:
        ...
