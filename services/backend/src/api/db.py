"""Module that contains DB related logic"""

import sqlalchemy
from databases import Database
from sqlalchemy.orm import sessionmaker

from .config import DATABASE_URL

from sqlalchemy.ext.declarative import declarative_base

database = Database(DATABASE_URL)  # initialize DB
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL, pool_size=3)

# Base = declarative_base()
#
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# database = SessionLocal()
