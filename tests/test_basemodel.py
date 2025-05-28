#!/usr/bin/python3
""" This module is to test bthe basemodel module
"""


from models import base_model
import unittest
import datetime


class test_base(unittest.TestCase):
    """ This test the instance variables of the base_model class
    """

    def setUp(self):
        """ Make these users for each test
        """

        self.user1 = base_model.BaseModel()
        self.user2 = base_model.BaseModel()

    def tearDown(self):
        """ destroy the users after each test
        """

        del self.user1
        del self.user2

    def test_variables(self):
        """ This function tests for the existence of
        some instance variables
        """

        self.assertIsNotNone(self.user1.id, msg="id doesn't exist")
        self.assertIsNotNone(self.user1.created_at, msg="created_at not exist")
        self.assertIsNotNone(self.user1.updated_at, msg="updated_at not there")

    def test_vartype(self):
        """ This function checks the type of variables
        """

        self.assertIsInstance(self.user1.id, str)
        self.assertIsInstance(self.user1.created_at, datetime.datetime)
        self.assertIsInstance(self.user1.updated_at, datetime.datetime)
