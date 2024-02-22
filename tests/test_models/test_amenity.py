#!/usr/bin/python3
""" This module testa Amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Amenity class test """

    def __init__(self, *args, **kwargs):
        """ Initializing  """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ test name type """
        new = self.value()
        self.assertEqual(type(new.name), str)
