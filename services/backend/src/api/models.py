"""Module that contains the model definition"""
import sqlalchemy
from sqlalchemy import Column, Integer, String

from .db import metadata


# class DictionaryModel(Base):
#     """Dictionary Model Definition"""
#     __tablename__ = "dictionary"
#     __table_args__ = {'extend_existing': True}
#
#     id = Column(Integer, primary_key=True, index=True)
#     dutch = Column(String)
#     english = Column(String)

dictionary = sqlalchemy.Table(
    "dictionary",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("dutch", sqlalchemy.String(150)),
    sqlalchemy.Column("english", sqlalchemy.String(150)),
    sqlalchemy.Column("part_of_speech", sqlalchemy.String(50)),
)
