"""Module that will keep logic of reading a file and inserting data from it"""
import asyncio
import json

from services.backend.src import database
from services.backend.src.api.repository import DictionaryRepository


async def populate_db():
    """Reads .json file and add entry to DB"""
    dictionary_repository = DictionaryRepository(database)
    with open("dictionary_database.json") as file_handler:
        for entry in json.load(file_handler):
            await dictionary_repository.create_dictionary_entry(**entry)


if __name__ == "__main__":
    asyncio.run(populate_db())
