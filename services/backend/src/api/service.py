"""Service App definition"""
import json
import logging

import requests
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .db import database, metadata, engine
from .repository import DictionaryRepository
from .views import router
# from services.bot.src.tg import DutchTeacherBot

logger = logging.getLogger(__name__)


class Application:
    """Main Application Class Definition.
    This Class contains all the application initial setup configuration that is run on app start up
    """

    # @staticmethod
    # def start_telegram_bot():
    #     """Telegram Bot Starting Point"""
    #
    #     t = DutchTeacherBot()
    #     t.register_commands()
    #     t.register_cronjobs()

    def run(self):
        """This method contains the initial setup configuration that is run on app start up"""

        app = FastAPI()

        # metadata.create_all(bind=engine)  # this is to create our models in the DB

        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )

        async def connect_to_db():
            # def connect_to_db():
            """
            Callback that will create a connection pool to the database on app start up
            """
            try:
                app.state.db = database
                await database.connect()
                # yield database
                logger.warning("--- DB CONNECTION CREATED ---")
            except Exception as e:
                logger.warning("--- DB CONNECTION ERROR ---")
                logger.warning(e)
                logger.warning("--- DB CONNECTION ERROR ---")

        async def close_db_connection():
            # def close_db_connection():
            """
            Callback that will close the connection pool to the database on app shutdown
            """
            try:
                await database.disconnect()
                # database.close()
            except Exception as e:
                logger.warning("--- DB DISCONNECT ERROR ---")
                logger.warning(e)
                logger.warning("--- DB DISCONNECT ERROR ---")

        async def populate_db():
            """Reads .json file and add entry to DB
                Called only once when we want to add some date in DB"""
            dictionary_repository = DictionaryRepository(database)
            with open("dictionary_database.json") as file_handler:
                data = json.load(file_handler)
            try:
                # r = requests.get("http://bot:8080/api/v1/bot/get_data").json()
                # for entry in r["result"]:
                for entry in json.load(data):
                    await dictionary_repository.create_dictionary_entry(**entry)
            except Exception as e:
                logger.warning("Error Writing Data")
                logger.warning(e)

        app.include_router(router, prefix="/api/v1/dictionary")

        app.add_event_handler("startup", connect_to_db)
        # app.add_event_handler("startup", self.start_telegram_bot)
        app.add_event_handler("startup", populate_db)
        app.add_event_handler("shutdown", close_db_connection)

        return app
