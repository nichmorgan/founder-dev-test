from typing import TypeVar, Generic
from pydantic import BaseModel, ConfigDict, Field
from enum import Enum


T = TypeVar("T")


class NodeTypes(str, Enum):
    START = "start"
    IF = "if"
    SET = "set"


class Edge(BaseModel):
    model_config = ConfigDict(extra="allow")

    source: str
    source_handle: str | None = Field(default=None, alias="sourceHandle")

    target: str


class Node(BaseModel, Generic[T]):
    model_config = ConfigDict(extra="allow")

    id: str
    data: T
    type: NodeTypes | str | None


class Flow(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str
    edges: list[Edge]
    nodes: list[Node]

    def get_node_by_id(self, id: str) -> Node:
        for node in self.nodes:
            if node.id == id:
                return node
        raise ValueError(f"Id '{id}' not found.")
