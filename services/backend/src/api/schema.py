"""
Module that is responsible for Pydantic Model Definition.
Grace to Pydantic models, the input data will be validated, serialized (converted), and annotated
"""
from pydantic import BaseModel


class DictionarySchema(BaseModel):
    """Class that is responsible for data validation"""
    id: int
    dutch: str
    english: str
    part_of_speech: str

    class Config:
        """The line 'orm_mode = True' allows the app to take ORM objects and translate them into responses automatically.
        This automation saves us from manually taking data out of ORM, making it into a dictionary,
        then loading it in with Pydantic."""
        orm_mode = True


class DictionaryInSchema(BaseModel):
    """Class that is responsible for data validation"""
    dutch: str
    english: str
    part_of_speech: str

    class Config:
        """The line 'orm_mode = True' allows the app to take ORM objects and translate them into responses automatically.
        This automation saves us from manually taking data out of ORM, making it into a dictionary,
        then loading it in with Pydantic."""
        orm_mode = True
