#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    """
    User class that inherits from BaseModel

    arguments: from BaseModel class as parent class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for User class"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return a string representation of the User instance"""
        return "[User] ({}) {} {}".format(self.id, self.first_name, self.last_name)
