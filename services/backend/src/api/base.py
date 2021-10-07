"""Base Setup Module"""
import sqlalchemy
from databases import Database

from .config import DATABASE_URL

database = Database(DATABASE_URL)  # initialize DB

metadata = sqlalchemy.MetaData()
