"""Module that will start the application"""

from fastapi import FastAPI

from tg import DutchTeacherBot

from views import router

app = FastAPI()


def start_tg_bog():
    """Method responsible for starting the TG bot"""
    t = DutchTeacherBot()
    # t.register_commands()
    t.register_cronjobs()


app.include_router(router, prefix="/api/v1/bot")
app.add_event_handler("startup", start_tg_bog)
