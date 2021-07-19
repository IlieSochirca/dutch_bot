"""Module where all app routes(urls) will be listed"""
import json

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    """Method that is checking if server is running and return Telegram User Info"""
    return {"Message": "Active Bot!", "status": 200}


@router.get("/get_data")
async def insert_data():
    """This endpoint will be called only when we need to insert data in DB """
    with open("data/dictionary_database.json") as file_handler:
        data = json.load(file_handler)
    return {"result": data}

