from fastapi.testclient import TestClient
import pytest
from typing import Any
from pydantic import BaseModel
from app.engine.configs.if_node_config import IfNodeConfig, IfOperator
from app.engine.configs.set_node_config import SetNodeConfig
from app.engine.configs.start_node_config import StartNodeConfig
from app.engine.executors.if_node_executor import TargetHandle
from app.engine.service import EngineService

from app.models.flow import Edge, Flow, Node, NodeTypes
from app.db.session import flow_collection


class TestData(BaseModel):
    title: str | None = None
    flow: Flow
    payload: dict
    expected_result: Any


def id_fn(context: TestData) -> str | None:
    return context.title


TEST_START_NODE = Node(
    id="start",
    data=StartNodeConfig(inputPath="a").model_dump(by_alias=True),
    type=NodeTypes.START,
)
TEST_IF_NODE = Node(
    id="if",
    type=NodeTypes.IF,
    data=IfNodeConfig(
        path="b",
        operator=IfOperator.eq,
        value=True,
    ).model_dump(by_alias=True),
)
TEST_SET_TRUE_NODE = Node(
    id="set_true",
    type=NodeTypes.SET,
    data=SetNodeConfig(path="", value=True).model_dump(by_alias=True),
)
TEST_SET_FALSE_NODE = Node(
    id="set_false",
    type=NodeTypes.SET,
    data=SetNodeConfig(path="", value=False).model_dump(by_alias=True),
)


TEST_DATA_LIST: list[TestData] = [
    TestData(
        title=f"sample {value}",
        flow=Flow(
            id="flow",
            nodes=[
                TEST_START_NODE,
                TEST_IF_NODE,
                TEST_SET_TRUE_NODE,
                TEST_SET_FALSE_NODE,
            ],
            edges=[
                Edge(
                    source=TEST_START_NODE.id,
                    target=TEST_IF_NODE.id,
                ),
                Edge(
                    source=TEST_IF_NODE.id,
                    sourceHandle=TargetHandle.yes,
                    target=TEST_SET_TRUE_NODE.id,
                ),
                Edge(
                    source=TEST_IF_NODE.id,
                    sourceHandle=TargetHandle.no,
                    target=TEST_SET_FALSE_NODE.id,
                ),
            ],
        ),
        payload={"a": {"b": value}},
        expected_result=value,
    )
    for value in [True, False]
]


@pytest.mark.parametrize("context", TEST_DATA_LIST, ids=id_fn)
def test_service(context: TestData):
    executor = EngineService(context.flow)
    result = executor.execute(context.payload)

    assert result == context.expected_result


# TODO: Move this to API module
@pytest.mark.parametrize("context", TEST_DATA_LIST, ids=id_fn)
def test_endpoint(client: TestClient, context: TestData):
    flow = context.flow
    flow_collection.insert_one(flow.model_dump(by_alias=True))

    response = client.post(f"/flow/execute/{flow.id}", json=context.payload)

    assert response.json() == context.expected_result
