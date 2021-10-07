"""Module where all app routes(urls) will be listed"""
import json
import logging

from fastapi import APIRouter, Depends
from .repository import DictionaryRepository
from .db import get_repository
from .schema import DictionarySchema, DictionaryInSchema

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/health")
def health_check():
    """Method that is checking if server is running and return Telegram User Info"""
    return {"Message": "Active!", "status": 200}


@router.post("/insert_data", response_model=DictionarySchema)
async def insert_data(data: DictionaryInSchema,
                      dictionary_repo: DictionaryRepository = Depends(get_repository(DictionaryRepository))):
    """This endpoint will be called only when we need to insert data in DB """
    entry_id = await dictionary_repo.create_dictionary_entry(**data.dict())
    return {**data.dict(), "id": entry_id}


@router.post("/populate_database", response_model=DictionarySchema)
async def populate_db(dictionary_repo: DictionaryRepository = Depends(get_repository(DictionaryRepository))):
    """Private endpoint that will be called by admin to insert data in DB"""
    # read json file that contains data for DB
    with open("/srv/dutch_bot/backend/api/dictionary_database.json") as file_handler:
        data = json.load(file_handler)
    try:
        for entry in data:
            await dictionary_repo.create_dictionary_entry(**entry)
    except Exception as e:
        logger.warning("Error Writing Data: %s", e)
        logger.warning(e)


@router.get("/get_data")
async def get_random_entry(dictionary_repo: DictionaryRepository = Depends(get_repository(DictionaryRepository))):
    """This endpoint will be called to return random entry from DB"""
    return await dictionary_repo.get_random_data()
