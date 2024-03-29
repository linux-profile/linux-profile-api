import motor.motor_asyncio

from bson import ObjectId
from app.core.settings import set_up


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


async def get_mongodb():
    config = set_up()
    client = motor.motor_asyncio.AsyncIOMotorClient(
        config.get("NOSQL_DATABASE_URL"))
    return client.linux["profiles"]
