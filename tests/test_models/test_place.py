#!/usr/bin/python3
""" test place """
import unittest
from models.base_model import BaseModel
from models.place import Place
from models.user import User
from models.city import City

from io import StringIO


class TestPlace(unittest.TestCase):
    """ unittest for place file """

    def test_instance(self):
        """test the creation of a Place instance"""
        p = Place()
        self.assertTrue(hasattr(p, 'city_id'))
        self.assertTrue(hasattr(p, 'user_id'))
        self.assertTrue(hasattr(p, 'name'))
        self.assertTrue(hasattr(p, 'description'))
        self.assertTrue(hasattr(p, 'number_rooms'))
        self.assertTrue(hasattr(p, 'number_bathrooms'))
        self.assertTrue(hasattr(p, 'max_guest'))
        self.assertTrue(hasattr(p, 'price_by_night'))
        self.assertTrue(hasattr(p, 'latitude'))
        self.assertTrue(hasattr(p, 'longitude'))
        self.assertTrue(hasattr(p, 'amenity_ids'))
        self.assertTrue(type(p.city_id), str)
        self.assertTrue(type(p.user_id), str)
        self.assertTrue(type(p.name), str)
        self.assertTrue(type(p.description), str)
        self.assertTrue(type(p.number_rooms), int)
        self.assertTrue(type(p.number_bathrooms), int)
        self.assertTrue(type(p.max_guest), int)
        self.assertTrue(type(p.price_by_night), int)
        self.assertTrue(type(p.latitude), float)
        self.assertTrue(type(p.longitude), float)
        self.assertTrue(type(p.amenity_ids), list)
        self.assertEqual(p.city_id, '')
        self.assertEqual(p.user_id, '')
        self.assertEqual(p.name, '')
        self.assertEqual(p.description, '')
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertEqual(p.amenity_ids, [])
        self.assertEqual(len(p.amenity_ids), 1)

        b = City()
        p.city_id = b.id
        self.assertEqual(p.city_id, b.id)
        c = User()
        p.user_id = c.id
        self.assertEqual(p.user_id, c.id)

    def test_city_id(self):
        place = Place()
        place.city_id = "42"
        self.assertEqual(place.city_id, "42")

    def test_user_id(self):
        place = Place()
        place.user_id = "0626839210"
        self.assertEqual(place.user_id, "0626839210")

    def test_name(self):
        place = Place()
        place.name = "San Francisco"
        self.assertEqual(place.name, "San Francisco")

    def test_description(self):
        place = Place()
        place.description = "La maison de Julien Cyr"
        self.assertEqual(place.description, "La maison de Julien Cyr")

    def test_number_rooms(self):
        place = Place()
        place.number_rooms = 6
        self.assertEqual(place.number_rooms, 6)

    def test_bathrooms(self):
        place = Place()
        place.number_bathrooms = 3
        self.assertEqual(place.number_bathrooms, 3)

    def test_max_guest(self):
        place = Place()
        place.max_guest = 18
        self.assertEqual(place.max_guest, 18)

    def test_price_by_night(self):
        place = Place()
        place.price_by_night = 300
        self.assertEqual(place.price_by_night, 300)

    def test_latitude(self):
        place = Place()
        place.latitude = 37.77750
        self.assertEqual(place.latitude, 37.77750)

    def test_longitude(self):
        place = Place()
        place.longitude = -122.41639
        self.assertEqual(place.longitude, -122.41639)

    def test_amenity_ids(self):
        place = Place()
        place.amenity_ids = ["Computer", "Wifi", "Coffee Machine"]
        self.assertEqual(place.amenity_ids, [
                         "Computer", "Wifi", "Coffee Machine"])
