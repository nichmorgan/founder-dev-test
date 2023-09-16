from app.engine.executors.start_node_executor import StartNodeExecutor, StartNodeConfig
from app.models.flow import Edge
import pytest

from tests.engine.utils import (
    get_default_payload,
    get_default_source,
    TestData,
    factory_executor,
    id_fn,
)


NodeTestData = TestData[StartNodeConfig]
TEST_DATA: list[NodeTestData] = [
    NodeTestData(
        title="sample",
        edges=[Edge(source=get_default_source(), target="321")],
        config=StartNodeConfig(inputPath="a"),
        expected_edge_index=0,
        expected_result=get_default_payload()["a"],
    )
]


@pytest.mark.parametrize("context", TEST_DATA, ids=id_fn)
def test(context: NodeTestData):
    factory_executor(context, StartNodeExecutor)
