
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from core.config import settings


client = MongoClient(settings.DATABASE_URL, server_api=ServerApi('1'))
db = client["notebook"]
collection = db["notes"]
