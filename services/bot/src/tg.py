"""Module that contains all Telegram Bot logic"""
import datetime
import logging
import os

import requests
from telegram.ext import Updater, CommandHandler, CallbackContext


class DutchTeacherBot:
    """Dutch Teacher Bot class definition. It will contain all Object specific attributes and methods"""

    def __init__(self):
        self.token = os.environ.get("TELEGRAM_TOKEN", None)
        self.user_id = os.environ.get("TELEGRAM_USER_ID", None).split(":")
        self.chat_id = os.environ.get("CHAT_ID", None)

        self.updater = Updater(token=self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

        # LOGGER CONFIGURATION
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

        self.logger = logging.getLogger(__name__)

        self.register_commands()

    def start(self, update, context) -> None:
        """
        Functionality of "START" command
        :param context:
        """
        update.message.reply_text('Welcome to the bot')

    def error(self, update, context):
        """Log Errors caused by Updates."""
        self.logger.warning('Update "%s" caused error "%s"', update, context.error)

    def register_commands(self) -> None:
        """
        Give a name to the command and add it to the dispatcher
        :return: None
        """
        start_handler = CommandHandler('start', self.start)
        self.dispatcher.add_handler(start_handler)
        self.updater.start_polling()  # enable bot to get updates

    def once(self, context: CallbackContext):
        """Test Method that will be called once
            This needs to make a request to "backend" container asking for data"""

        result = requests.get("http://backend:8080/api/v1/dictionary/get_data").json()

        context.bot.send_message(chat_id=self.chat_id,
                                 text=f"-Dutch: {result['dutch']}\n-English: {result['english']}")

    def register_cronjobs(self) -> None:
        """This method is registering methods"""
        j = self.updater.job_queue
        # j.run_daily(self.once, days=tuple(range(7)), time=datetime.time(hour=19, minute=1, second=00))
        # j.run_daily(self.once, days=tuple(range(7)), time=datetime.time(hour=17, minute=1, second=00))
        # j.run_daily(self.once, days=tuple(range(7)), time=datetime.time(hour=14, minute=1, second=00))
        # j.run_daily(self.once, days=tuple(range(7)), time=datetime.time(hour=12, minute=1, second=00))
        # j.run_daily(self.once, days=tuple(range(7)), time=datetime.time(hour=9, minute=1, second=00))
        # j.run_daily(self.once, days=tuple(range(7)), time=datetime.time(hour=7, minute=1, second=00))
        j.run_daily(self.once, days=tuple(range(7)), time=datetime.time(hour=16, minute=54, second=00))


if __name__ == "__main__":
    t = DutchTeacherBot()
    t.register_commands()
    t.register_cronjobs()

# DOCUMENTATION
# https://medium.com/analytics-vidhya/python-telegram-bot-with-scheduled-tasks-932edd61c534
