from typing import TypeVar, Generic
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum

T = TypeVar("T")
BASE_CONFIG = ConfigDict(extra="allow")


class NodeTypes(str, Enum):
    START = "start"
    IF = "if"
    SET = "set"


class Edge(BaseModel):
    model_config = BASE_CONFIG

    source: str
    target: str


class Node(BaseModel, Generic[T]):
    model_config = BASE_CONFIG

    id: str
    data: T
    type: NodeTypes | str | None


class Flow(BaseModel):
    model_config = BASE_CONFIG

    id: str
    edges: list[Edge]
    nodes: list[Node]
