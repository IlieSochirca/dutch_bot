"""Module where all app routes(urls) will be listed"""
from fastapi import APIRouter

from .db import database

from .repository import DictionaryRepository
from .schema import DictionarySchema, DictionaryInSchema

router = APIRouter()
dictionary_repository = DictionaryRepository()
# dictionary_repository = DictionaryRepository(database)


@router.get("/health")
def health_check():
    """Method that is checking if server is running and return Telegram User Info"""
    return {"Message": "Active!", "status": 200}


@router.post("/insert_data", response_model=DictionarySchema)
async def insert_data(data: DictionaryInSchema):
    """This endpoint will be called only when we need to insert data in DB """
    entry_id = await DictionaryRepository.create_dictionary_entry(**data.dict())
    return {**data.dict(), "id": entry_id}


@router.get("/get_data")
async def get_random_entry():
    """This endpoint will be called to return random entry from DB"""
    return await DictionaryRepository.get_random_data()
