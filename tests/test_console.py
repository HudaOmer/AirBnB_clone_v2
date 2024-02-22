#!/usr/bin/python3
"""test for console"""
import unittest
import console


class test_Console(unittest.TestCase):
    """ test consol class """

    def test_documentation(self):
        """ test if doc exists """
        self.assertIsNotNone(console.__doc__)
