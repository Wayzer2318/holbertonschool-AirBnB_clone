#!/usr/bin/python3
import unittest
import datetime
from models.base_model import BaseModel


class TestModelBase(unittest.TestCase):
    def setUp(self):
        self.instance = BaseModel()

    def test_id_is_str(self):
        self.assertEqual(str(type(self.instance.id)), "<class 'str'>")

    def test_created_is_dtobj(self):
        strtst = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(self.instance.created_at)), strtst)

    def test_updated_is_dtobj(self):
        strtst2 = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(self.instance.updated_at)), strtst2)

    def test_save_isdtobj(self):
        strtst2 = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(self.instance.save)), strtst2)
