#!/usr/bin/python3
""" This module is to test the basemodel module
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
#        self.assertIsInstance(self.user1.created_at, datetime.datetime)
#        self.assertIsInstance(self.user1.updated_at, datetime.datetime)

    def test_str(self):
        """ Testing the methods of the class
        """

        retstr = str(self.user1)
        teststr = f"[BaseModel] ({self.user1.id}) {self.user1.__dict__}"
        if (retstr):
            pass
        else:
            raise ValueError("str dunder method not available")
        if retstr != teststr:
            raise ValueError("The given strings don't match")

    def test_save(self):
        """This function tests the save method
        """

        self.user1.save()
        if self.user1.updated_at == self.user1.created_at:
            raise ValueError("updated_at was not updated when save was called")

    def test_to_dict(self):
        """Test the to_dict method
        The method takes no arguments
        """

        checkdict = self.user1.to_dict()
        self.assertIsInstance(checkdict, dict)
        """print(checkdict)"""
        if '__class__' not in checkdict:
            raise ValueError("__class__ key not present")
        if (checkdict["__class__"] != "BaseModel"):
            raise ValueError("key of __class__ not class name")
        if (type(checkdict["created_at"]) is not str):
            raise TypeError("type of created_at is not str")
        if (type(checkdict["updated_at"]) is not str):
            raise TypeError("Type of updated_at is not str")

    def test_new_init(self):
        """ This function tests whethere the updated init works
        well. It assigns new attributes as the key to the dict
        it also gives their values as the attribute values.
        """

        checkdict = self.user1.to_dict()
        user3 = base_model.BaseModel(**checkdict)
        for key in checkdict.keys():
            if key == "__class__":
                continue
            if not hasattr(user3, key):
                print(key)
                print(user3.__dict__)
                print("\n\n\n")
                raise ValueError(f"Attribute {key} not found")
        for key, value in checkdict.items():
            if key == "__class__":
                continue
            val = getattr(user3, key, None)
            if user3.__dict__[key] != val:
                print(f"The key is {key} ")
                print(f"The value is {value} ")
                print(f"The attribute is {val} ")
                raise ValueError(f"Value in the dict dont match the attr")
