#!/usr/bin/python3
""" tests for file storage """
import unittest
import os
import json


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ test for file storage """

    def setup(self):
        """ set up """
        self.my_model = BaseModel()
        self.my_storage = FileStorage()

    def tear_down(self):
        """ tear down method """
        if os.path.exists("file.json"):
            os.remove("file.json")
        else:
            pass

    def test_instance(self):
        """ test for storage class instance creation """
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_new(self):
        """ test new """
        self.my_storage.new(self.my_model)
        new_dict = self.my_storage.all()
        key = self.my_model.__class__.__name__ + "." + self.my_model.id
        self.assertIsInstance(new_dict[key], BaseModel)

    def test_all(self):
        """ test all """
        self.assertIsInstance(self.my_storage.all(), dict)

    def test_save(self):
        """ test save """
        self.my_storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """ test for file storage reloading """
        self.my_storage.save()
        s = FileStorage()
        s.reload()
        kx = s.__objects.keys()
        ky = self.my_storage.__objects.keys()
        self.assertTrue(kx, ky)

    def test_content_type(self):
        """ test content type """
        self.my_storage.save()
        self.my_storage.new(self.my_model)

        with open("file.json", encoding='utf-8') as f:
            content = json.load(f)

        self.assertIsInstance(content, dict)
