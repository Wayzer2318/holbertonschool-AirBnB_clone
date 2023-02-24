#!/usr/bin/python3
""" test base model """
import unittest
import datetime
from models.base_model import BaseModel


class TestModelBase(unittest.TestCase):
    """ test model base """

    def setUp(self):
        self.instance = BaseModel()

    def test_to_dict(self):
        v = self.instance.to_dict()
        self.assertEqual(type(v), dict)

        self.assertTrue('__class__' in v)
        self.assertEqual(v['__class__'], self.instance.__class__.__name__)

    def test_id_is_str(self):
        self.assertEqual(type(self.instance.id), str)
        self.assertEqual(self.instance.id.count('-'), 4)

    def test_created_is_dtobj(self):
        strtst = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(self.instance.created_at)), strtst)

    def test_updated_is_dtobj(self):
        strtst2 = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(self.instance.updated_at)), strtst2)

    def test_save_isdtobj(self):
        date = self.instance.updated_at.isoformat()
        self.instance.save()
        self.assertNotEqual(self.instance.updated_at.isoformat(), date)
