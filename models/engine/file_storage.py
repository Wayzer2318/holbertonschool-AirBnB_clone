#!/usr/bin/python3
""" engine storage """
import json


from models.base_model import BaseModel


class FileStorage():
    """ file storage class """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """ register new object """

        k = ''

        k += obj.__class__.__name__
        k += '.'
        k += obj.id

        FileStorage.__objects[k] = obj

    def save(self):
        """ save all objects to fs """

        data = {
            k: v.to_dict()
            for k, v in FileStorage.__objects.items()
        }

        p = FileStorage.__file_path
        with open(p, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def reload(self):
        """ reload all objects from fs """

        p = FileStorage.__file_path
        try:
            with open(p, 'r', encoding='utf-8') as file:
                data = json.load(file)

        except FileNotFoundError:
            return

        FileStorage.__objects = {
            k: globals()[k.split('.')[0]](**v)
            for k, v in data.items()
        }
