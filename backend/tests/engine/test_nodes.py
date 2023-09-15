from app.engine.nodes.base import NodeConfig
from app.engine.nodes.if_node import IfNode, IfNodeConfig, IfOperator, TargetHandle
from app.engine.nodes.start_node import StartNode, StartNodeConfig
from app.models.flow import Edge
import pytest


@pytest.fixture
def payload():
    return {"a": {"b": 1}}


def test_start_node(payload):
    edges: list[Edge] = [Edge(source="123", target="321")]
    config = StartNodeConfig.model_validate({"inputPath": "a"})

    node = StartNode(NodeConfig(config=config, edges=edges))
    result = node.execute(payload)

    assert result.data == payload["a"]
    assert result.next_nodes == set([edges[0].target])


# TODO: Create if node tests!


def test_if_eq_node(payload):
    source = "1"
    expected_edge = Edge(source=source, target="2", sourceHandle=TargetHandle.yes)
    edges: list[Edge] = [
        expected_edge,
        Edge(source=source, target="3", sourceHandle=TargetHandle.no),
    ]

    config = IfNodeConfig(path="a.b", operator=IfOperator.eq, value=payload["a"]["b"])
    node = IfNode(NodeConfig(config=config, edges=edges))

    result = node.execute(payload)

    assert result.data == payload
    assert result.next_nodes == set([expected_edge.target])
