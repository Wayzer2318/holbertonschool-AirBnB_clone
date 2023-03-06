#!/usr/bin/python3
""" test state """
import unittest
from models.review import Review


class ReviewTest(unittest.TestCase):
    """ test for state """

    def test_instance(self):
        instance = Review()
        self.assertIsInstance(instance, Review)

    def test_id(self):
        instance = Review()
        self.assertEqual(str, type(instance.id))

    def test_place_id(self):
        instance = Review()
        self.assertEqual(instance.place_id, '')

    def test_user_id(self):
        instance = Review()
        self.assertEqual(instance.user_id, '')

    def test_text(self):
        instance = Review()
        self.assertEqual(instance.text, '')
