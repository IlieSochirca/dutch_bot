"""Service App definition"""
import logging

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .views import router
from .tasks import create_start_app_handler, create_stop_app_handler, start_telegram_bot

logger = logging.getLogger(__name__)


class Application:
    """Main Application Class Definition.
    This Class contains all the application initial setup configuration that is run on app start up
    """

    def run(self):
        """This method contains the initial setup configuration that is run on app start up"""

        app = FastAPI()

        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )

        app.include_router(router, prefix="/api/v1/dictionary")

        app.add_event_handler("startup", create_start_app_handler(app))
        app.add_event_handler("shutdown", create_stop_app_handler(app))
        app.add_event_handler("startup", start_telegram_bot)

        return app
