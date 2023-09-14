from fastapi import status
from fastapi.testclient import TestClient
from app.models.flow import Flow
from app.db.session import flow_collection
from tests.fixtures.factories import FlowFactory


def test_save(client: TestClient, flow_factory: FlowFactory):
    flow: Flow = flow_factory.build()
    flow_json = flow.model_dump(by_alias=True)

    # Extra Fields
    extra_field = "extra1"
    flow_json[extra_field] = "any"

    response = client.put("/flow/save", json=flow_json)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    flowInDb = flow_collection.find_one({"id": flow.id})
    assert flowInDb is not None
    assert extra_field in flowInDb


def test_restore(client: TestClient, flow_factory: FlowFactory):
    flow: Flow = flow_factory.build()

    flow_collection.insert_one(flow.model_dump())

    response = client.get(f"/flow/restore/{flow.id}")
    assert response.status_code == status.HTTP_200_OK
    assert Flow.model_validate(response.json()) == flow


def test_restore_fail(client: TestClient):
    response = client.get("/flow/restore/abc")
    assert response.status_code == status.HTTP_404_NOT_FOUND