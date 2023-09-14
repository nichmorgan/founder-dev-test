from fastapi import status
from app.models.flow import Flow
from app.db.session import flow_collection


def test_save(client, flow_factory):
    flow: Flow = flow_factory.build()

    response = client.put("/flow/save", json=flow.model_dump(by_alias=True))
    assert response.status_code == status.HTTP_204_NO_CONTENT

    flowInDb = flow_collection.find_one({"id": flow.id})
    assert flowInDb is not None
