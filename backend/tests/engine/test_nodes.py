from app.engine.nodes.start_node import StartNode, StartNodeConfig
from app.models.flow import Edge


def test_start_node():
    data = {"a": {"b": 1}}
    edges: list[Edge] = [Edge(source="123", target="321")]
    config = StartNodeConfig.model_validate({"inputPath": "a"})

    node = StartNode(config, edges)
    result = node.execute(data)

    assert result.data == data["a"]
    assert result.next_nodes == set([edges[0].target])
