"""This module will contain the entrypoint to all SQL functions for this DB model, following DAL(Data Access Layer)"""
from fastapi import Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from .db import database
from .models import dictionary
from .schema import DictionarySchema


class DictionaryRepository:
    """
    Class that is implementing the Data Access Layer, all the interaction with the DB will stay here.
    """

    def __init__(self, db_session: Session = Depends(database)):
        self.db_session = db_session

    # def create_dictionary_entry(self, dictionary: DictionarySchema):
    #     """
    #     Method that is creating an entry of type "dictionary" in the DB
    #     :param dictionary:
    #     :return: new entry
    #     """
    #     new_entry = DictionaryModel(**dictionary.dict())
    #     self.db_session.add(new_entry)
    #     self.db_session.commit()
    #     self.db_session.refresh(new_entry)
    #     return new_entry

    @classmethod
    async def create_dictionary_entry(cls, **input_data):
        """
        Method that is creating an entry of type "dictionary" in the DB
        :param input_data:
        :return: New Entry
        """
        query = dictionary.insert().values(**input_data)
        return await database.execute(query)

    @classmethod
    async def get_random_data(cls):
        """
        Select random row with data from DB
        :return:
        """

        # TODO: fix random data selection
        # query = dictionary.select().where(dictionary.c.id == random.randint(0, 200))
        query = dictionary.select().order_by(func.random()).limit(5)
        record = await database.fetch_one(query)
        return DictionarySchema(**record)

# Documentation
# following: https://towardsdatascience.com/build-an-async-python-service-with-fastapi-sqlalchemy-196d8792fa08

