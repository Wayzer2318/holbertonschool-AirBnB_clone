#!/usr/bin/python3
""" test state """
import unittest
from models.amenity import Amenity


class AmenityTest(unittest.TestCase):
    """ test for state """

    def test_name_is_str(self):
        instance = Amenity()
        self.assertEqual(instance.name, "")

    def test_instance(self):
        instance = Amenity()
        self.assertIsInstance(instance, Amenity)

    def test_id(self):
        instance = Amenity()
        self.assertEqual(str, type(instance.id))
