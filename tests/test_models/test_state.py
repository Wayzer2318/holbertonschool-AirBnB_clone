#!/usr/bin/python3
""" test state """
import unittest
from models.state import State


class StateTest(unittest.TestCase):
    """ test for state """

    def test_name_is_str(self):
        instance = State()
        self.assertEqual(instance.name, "")

    def test_instance(self):
        instance = State()
        self.assertIsInstance(instance, State)

    def test_id(self):
        instance = State()
        self.assertEqual(str, type(instance.id))
