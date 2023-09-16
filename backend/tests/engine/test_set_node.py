from app.engine.executors.set_node_executor import SetNodeExecutor, SetNodeConfig
from app.models.flow import Edge
import pytest
import pydash

from tests.engine.utils import (
    get_default_source,
    get_default_payload,
    TestData,
    factory_executor,
    id_fn,
)


NodeTestData = TestData[SetNodeConfig]
INSERT_TEST_DATA_CONFIG = SetNodeConfig(path="a.c", value=2)
INSERT_NODE_TEST_DATA = NodeTestData(
    title="insert",
    edges=[Edge(source=get_default_source(), target="321")],
    config=INSERT_TEST_DATA_CONFIG,
    expected_edge_index=0,
    expected_result=pydash.set_(
        get_default_payload(),
        INSERT_TEST_DATA_CONFIG.path,
        INSERT_TEST_DATA_CONFIG.value,
    ),
)

OVERRIDE_NODE_TEST_DATA = NodeTestData(
    **INSERT_NODE_TEST_DATA.model_dump(by_alias=True)
)
OVERRIDE_NODE_TEST_DATA.title = "override"
OVERRIDE_NODE_TEST_DATA.config.path = "a"
OVERRIDE_NODE_TEST_DATA.expected_result = {"a": OVERRIDE_NODE_TEST_DATA.config.value}

TEST_DATA: list[NodeTestData] = [INSERT_NODE_TEST_DATA, OVERRIDE_NODE_TEST_DATA]


@pytest.mark.parametrize("context", TEST_DATA, ids=id_fn)
def test(context: NodeTestData):
    factory_executor(context, SetNodeExecutor)
