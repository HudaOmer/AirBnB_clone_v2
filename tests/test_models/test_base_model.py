#!/usr/bin/python3
""" this module to test base model """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") == "db",
    "Test is not relevant for BaseModel"
)
class test_basemodel(unittest.TestCase):
    """ test class """

    def __init__(self, *args, **kwargs):
        """document  documt"""
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def setUp(self):
        """document d ocumt"""
        pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_default(self):
        """document d  ocumt"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """docu ment documt"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """docu ment documt"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Testing s ave"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open("file.json", "r") as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """docume nt documt"""
        i = self.value()
        self.assertEqual(str(i), "[{}] ({}) {}".
                         format(self.name, i.id, i.__dict__))

    def test_todict(self):
        """documen  t documt"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """docu ment documt"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """document  documt"""
        n = {"name": "nuux"}
        new = self.value(**n)
        self.assertEqual(new.name, n["name"])

    def test_id(self):
        """docu  ment documt"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """docum ent documt"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """docum ent documt"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        new.save()
        self.assertFalse(new.created_at == new.updated_at)
