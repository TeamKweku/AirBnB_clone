#!/usr/bin/python3
""" a module that implements a class FileStorage for creating persisting data
ie. handles serialization and deserialization of dict and JSON files
"""
import json


class FileStorage:
    """This is an implementation of the FileStorae class

    Attributes:
        __file_path(str): path to the JSON file
        __objects(dict): empty dict that would store all objects by
                        <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """this method returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects obj with the key <obj_class_name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (__file_path)"""
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def reload(self):
        """deserialization of the JSON file to __objects if file exits"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                dict_obj = json.load(f)
                for key, value in dict_obj.items():
                    class_name, obj_id = key.split(".")
                    cls = globals()[class_name]
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj

        except FileNotFoundError:
            return
