#!/usr/bin/python3
""" this module tests review """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ a testing class for review """

    def __init__(self, *args, **kwargs):
        """ Initializing """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test id type """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Test id type for user"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Test text type"""
        new = self.value()
        self.assertEqual(type(new.text), str)
