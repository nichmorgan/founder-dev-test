from app.engine.executors.if_node_executor import (
    IfNodeExecutor,
    IfNodeConfig,
    IfOperator,
    TargetHandle,
)
from app.models.flow import Edge
import pytest

from tests.engine.utils import (
    get_default_source,
    get_default_payload,
    TestData,
    factory_executor,
    id_fn,
)

NodeTestData = TestData[IfNodeConfig]


def node_test_data_factory(operator: IfOperator, result: bool) -> NodeTestData:
    payload = get_default_payload()
    value = payload["a"]["b"]
    source = get_default_source()

    if result:
        if operator == IfOperator.lt:
            value += 1
        elif operator == IfOperator.gt:
            value -= 1
    else:
        if operator in [IfOperator.eq, IfOperator.gte]:
            value += 1
        elif operator == IfOperator.lte:
            value -= 1

    return NodeTestData(
        title=f"{IfOperator(operator).name}: {'Yes' if result else 'No'}",
        edges=[
            Edge(source=source, target="2", sourceHandle=TargetHandle.yes),
            Edge(source=source, target="3", sourceHandle=TargetHandle.no),
        ],
        config=IfNodeConfig(
            path="a.b",
            operator=operator,
            value=value,
        ),
        expected_edge_index=0 if result else 1,
        expected_result=payload,
    )


TEST_DATA = [
    node_test_data_factory(operator, result)
    for result in [True, False]
    for operator in list(IfOperator)
]


@pytest.mark.parametrize("context", TEST_DATA, ids=id_fn)
def test(context: NodeTestData):
    factory_executor(context, IfNodeExecutor)
