from app.engine.nodes.if_node import IfNode, IfNodeConfig, IfOperator, TargetHandle
from app.models.flow import Edge
import pytest

from tests.engine.utils import (
    DEFAULT_PAYLOAD,
    DEFAULT_SOURCE,
    TestData,
    factory_executor,
    id_fn,
)

NodeTestData = TestData[IfNodeConfig]

EQ_YES_TEST_DATA = NodeTestData(
    title="Eq: Yes",
    edges=[
        Edge(source=DEFAULT_SOURCE, target="2", sourceHandle=TargetHandle.no),
        Edge(source=DEFAULT_SOURCE, target="3", sourceHandle=TargetHandle.yes),
    ],
    config=IfNodeConfig(
        path="a.b", operator=IfOperator.eq, value=DEFAULT_PAYLOAD["a"]["b"]
    ),
    expected_edge_index=1,
    expected_result=DEFAULT_PAYLOAD,
)

EQ_NO_TEST_DATA = NodeTestData(**EQ_YES_TEST_DATA.model_dump(by_alias=True))
EQ_NO_TEST_DATA.title = "Eq: No"
EQ_NO_TEST_DATA.config.value += 1
EQ_NO_TEST_DATA.expected_edge_index = 0


EQ_TESTDATA: list[NodeTestData] = [
    EQ_YES_TEST_DATA,
    EQ_NO_TEST_DATA,
]


@pytest.mark.parametrize("context", EQ_TESTDATA, ids=id_fn)
def test_eq(context: NodeTestData):
    factory_executor(context, IfNode)
