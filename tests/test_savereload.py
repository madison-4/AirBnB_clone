#!/usr/bin/python3
"""This module is meant to test the new functions
save, reload and all. They pesist objects into the file storage
"""

from models.engine import file_storage
from models import base_model
import unittest
import os
import json

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
        path = os.getcwd()
        entries = os.listdir(os.getcwd())
        for fp in entries:
            checker = path + "/" + fp
            if (os.path.isfile(checker)):
                if checker.endswith('.json'):
                    break
        else:
            raise FileNotFoundError("No .json file created")
        with open(checker, "r") as fildes:
            try:
                with open(checker, "r") as fildes:
                    json.load(fildes)
            except json.JSONDecodeError as e:
                raise ValueError(f"Contents of {checker} aren't json valid")

    def test_reload(self):
        """ This function tests the reload function
        It checks the function does not fail if the file doesn't exist
        It then checks the contents of the private variable objects match those
        in the file.json

        First it deletes the files named .json
        """

        paths = os.getcwd()
        files = os.listdir(paths)
        for obj in files:
            to_del = paths + "/" + obj
            if os.path.isfile(to_del):
                if to_del.endswith(".json"):
                    os.remove(to_del)
        self.obj1.reload()
        val = self.obj1.all()

if __name__ == "__main__":
    unittest.main()
