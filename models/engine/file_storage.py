#!/usr/bin/python3
import json
from models.base_model import BaseModel
"""
class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""


class FileStorage:
    """
    filestorage class
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        adding to __objects
        """
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        save
        """
        data = {}
        for k, v in self.__objects.items():
            data[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """
        reload
        """
        data_dict = {}
        classes = {
            "BaseModel": BaseModel,
        }
        try:
            with open(self.__file_path, 'r') as f:
                data_dict = json.load(f)
                for k, v in data_dict.items():
                    self.__objects[k] = classes[v["__class__"]](**v)
        except FileNotFoundError:
            pass
