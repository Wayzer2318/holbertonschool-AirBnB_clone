#!/usr/bin/python3
""" test state """
import unittest
from models.city import City


class CityTest(unittest.TestCase):
    """ test for state """

    def test_name_is_str(self):
        instance = City()
        self.assertEqual(instance.name, "")

    def test_instance(self):
        instance = City()
        self.assertIsInstance(instance, City)

    def test_state_id(self):
        instance = City()
        self.assertEqual(str, type(instance.state_id))
        self.assertEqual('', instance.state_id)

    def test_id(self):
        instance = City()
        self.assertEqual(str, type(instance.id))
