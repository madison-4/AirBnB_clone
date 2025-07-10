#!/usr/bin/python3
"""This module is meant to test the new functions
save, reload and all. They pesist objects into the file storage
"""

from models.engine import file_storage
from models import base_model
import unittest
import os

class Testsave(unittest.TestCase):
    """ This class tests the persistence functions
    """

    def setUp(self):
        """ Make these users for each test so I can test well
        """

        self.obj1 = file_storage.FileStorage()
        self.obj2 = base_model.BaseModel()

    def tearDown(self):
        """ Delete the objects after each test
        """

        del self.obj1
        del self.obj2

    def test_all(self):
        """ This function tests the all function
        """

        ret = self.obj1.all()
        if (type(ret) is not dict):
            raise TypeError("all does not return a dictionary")
        self.assertIsInstance(ret, dict, msg="all should return a dict")

    def test_new(self):
        """ Tests the new function
        it checks the returned value is a non empty dictionary
        """

        self.obj1.new(self.obj2)
        ret = self.obj1.all()
        self.assertIsInstance(ret, dict, msg="all should give back a dict")
        self.assertNotEqual(len(ret), 0)

    def test_save(self):
        """ tests the save function is created
        """

        self.obj1.save()

if __name__ == "__main__":
    unittest.main()
