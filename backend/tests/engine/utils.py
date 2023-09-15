from typing import Any, Generic, Type, TypeVar
from pydantic import BaseModel, field_validator, FieldValidationInfo
from app.engine.nodes.base import NodeConfig
from app.engine.nodes.if_node import IfNode, IfNodeConfig
from app.engine.nodes.start_node import StartNode, StartNodeConfig
from app.models.flow import Edge

TNode = TypeVar("TNode", IfNode, StartNode)
TConfig = TypeVar("TConfig", IfNodeConfig, StartNodeConfig)

DEFAULT_PAYLOAD = {"a": {"b": 1}}
DEFAULT_SOURCE = "1"


class TestData(BaseModel, Generic[TConfig]):
    title: str | None = None
    edges: list[Edge] = []
    config: TConfig
    payload: dict = DEFAULT_PAYLOAD
    expected_edge_index: int | None = None
    expected_result: Any

    @field_validator("expected_edge_index")
    @classmethod
    def validate_edge_index(
        cls, index: int | None, info: FieldValidationInfo
    ) -> int | None:
        if index == None:
            return

        edges = info.data["edges"]
        if 0 > index >= len(edges):
            raise ValueError("index out of edges array bounds.")
        return index

    @property
    def node_config(self) -> NodeConfig[TConfig]:
        return NodeConfig(config=self.config, edges=self.edges)

    @property
    def expected_next_nodes(self) -> set[str]:
        if self.expected_edge_index is None:
            return set([])
        return set([self.edges[self.expected_edge_index].target])


def id_fn(test_data: TestData) -> str | None:
    return test_data.title


def factory_executor(context: TestData, node_factory: Type[TNode]):
    node = node_factory(context.node_config)
    result = node.execute(context.payload)

    assert result.data == context.expected_result
    assert result.next_nodes == context.expected_next_nodes
