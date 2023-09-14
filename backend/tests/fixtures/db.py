from app.core.config import settings
from pymongo_inmemory import MongoClient
import pytest


@pytest.fixture(autouse=True)
def setup_test_db():
    client = MongoClient(settings.MONGO_DATABASE_DSN.unicode_string())
    client.start_session()

    yield client  # type: ignore

    client.close()
