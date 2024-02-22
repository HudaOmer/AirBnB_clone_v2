#!/usr/bin/python3
""" This module is to test place class"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ a class to test place """

    def __init__(self, *args, **kwargs):
        """ Initializing """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Test the id type """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ test the id type for user """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ test the name """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Test the description """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ test room number type """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ test if integer """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ tset if integer """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """  Testif integer """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ latitude test"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ longitude tset  """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ aminity test """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
