#!/usr/bin/python3
"""module for creating an instance File Storage to be accessed by the program"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
