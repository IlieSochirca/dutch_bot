"""This module will contain the entrypoint to all SQL functions for this DB model, following DAL(Data Access Layer)"""
from sqlalchemy import func
from databases import Database
from .models import dictionary
from .schema import DictionarySchema


class BaseRepository:
    """Base Repository Implementation Class.
       Will be inherited by more other Repository Classes to follow
    """

    def __init__(self, db: Database) -> None:
        self.db = db


class DictionaryRepository(BaseRepository):
    """
    Class that is implementing the Data Access Layer, all the interaction with the DB will stay here.
    """

    async def create_dictionary_entry(self, **input_data):
        """
        Method that is creating an entry of type "dictionary" in the DB
        :param input_data:
        :return: New Entry
        """
        query = dictionary.insert().values(**input_data)
        return await self.db.execute(query)

    async def get_random_data(self):
        """
        Select random row with data from DB
        :return:
        """
        query = dictionary.select().order_by(func.random()).limit(5)
        record = await self.db.fetch_one(query)
        return DictionarySchema(**record)

# Documentation
# following: https://towardsdatascience.com/build-an-async-python-service-with-fastapi-sqlalchemy-196d8792fa08
