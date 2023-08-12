#!/usr/bin/python3
"""
Module for City class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class has BaseModel as parent.
    """

    state_id = ""
    name = ""
