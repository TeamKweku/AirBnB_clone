#!/usr/bin/python3
""" a module that implements the base model class that is inherited by all
other class
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """This is implementation of the BaseModel class

    Attributes:
        created_at(dateime): created instance date
        updated_at(datetime): updated time when instance is updated
    """

    def __init__(self, *args, **kwargs):
        """the instantation method of the class"""
        # copy_dict = kwargs.copy()
        str_rep = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        # if "__class__" in copy_dict.keys():
        # del copy_dict["__class__"]
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    new_value = datetime.strptime(kwargs[key], str_rep)
                    setattr(self, key, new_value)
                else:
                    setattr(self, key, value)
            storage.new(self)
        else:
            # self.id = str(uuid.uuid4())
            # self.created_at = datetime.now()
            # self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """This is the string representation of an instance of the
        BaseModel
        """
        base_str = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return base_str

    def save(self):
        """a method that updates the updated date when called on
        an instance
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """method that returns the instance attributes of an object in
        dictionary format
        """
        copy_dict = self.__dict__.copy()
        copy_dict["created_at"] = self.created_at.isoformat()
        copy_dict["updated_at"] = self.updated_at.isoformat()
        copy_dict["__class__"] = self.__class__.__name__

        return copy_dict
