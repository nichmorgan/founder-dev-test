from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

from app.core.config import settings


client: MongoClient = MongoClient(settings.MONGO_DATABASE_DSN.unicode_string())
db: Database = client[settings.MONGO_DATABASE_NAME]

flow_collection: Collection = db["flow"]
