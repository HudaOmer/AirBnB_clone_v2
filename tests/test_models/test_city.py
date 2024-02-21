#!/usr/bin/python3
""" A module for city class testing"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ this class tests City class """

    def __init__(self, *args, **kwargs):
        """ initialising """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ test for state id type """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ test the name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
