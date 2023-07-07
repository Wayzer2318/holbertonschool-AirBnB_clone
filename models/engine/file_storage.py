#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""
class FileStorage
"""


class FileStorage:
    """
    file storage class
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
        new
        """
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """save"""
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
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                data_dict = json.load(f)
                for k, v in data_dict.items():
                    self.__objects[k] = classes[v["__class__"]](**v)
        except FileNotFoundError:
            pass
