from app.engine.nodes.start_node import StartNode, StartNodeConfig
from app.models.flow import Edge
import pytest

from tests.engine.utils import (
    DEFAULT_PAYLOAD,
    DEFAULT_SOURCE,
    TestData,
    factory_executor,
    id_fn,
)


NodeTestData = TestData[StartNodeConfig]
TEST_DATA: list[NodeTestData] = [
    NodeTestData(
        title="sample",
        edges=[Edge(source=DEFAULT_SOURCE, target="321")],
        config=StartNodeConfig(inputPath="a"),
        expected_edge_index=0,
        expected_result=DEFAULT_PAYLOAD["a"],
    )
]


@pytest.mark.parametrize("context", TEST_DATA, ids=id_fn)
def test(context: NodeTestData):
    factory_executor(context, StartNode)
