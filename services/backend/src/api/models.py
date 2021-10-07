"""Module that contains the model definition"""
import sqlalchemy

from .base import metadata

dictionary = sqlalchemy.Table(
    "dictionary",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("dutch", sqlalchemy.String(150)),
    sqlalchemy.Column("english", sqlalchemy.String(150)),
    sqlalchemy.Column("part_of_speech", sqlalchemy.String(50)),
)
