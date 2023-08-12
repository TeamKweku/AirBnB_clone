#!/usr/bin/python3
from models.base_model import BaseModel

"""a module that implements the User model that inherits from BaseModel"""


class User(BaseModel):
    """
    User class that inherits from BaseModel

    arguments: from BaseModel class as parent class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
