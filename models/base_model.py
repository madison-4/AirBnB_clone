#!/usr/bin/python3
""" This module defines the base model for all the classes
"""


import uuid
from datetime import datetime
from . import storage

class BaseModel:
    """ This class defines the common attributes and methods
    All classes will inherit these methods
    """

    def __init__(self, *args, **kwargs):
        """ This method inmitilizes all objects
        It just assigns the id and the time using uuid
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at =self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Define how the instance should be printed
        """

        my_string = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
        return my_string

    def save(self):
        """ A function to save the instance and the time it is saved
        It simply updates the instance attribute updated_at
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance:

        - only instance attributes set will be returned
        - a key __class__ is added with the class name of the object
        - created_at and updated_at must be converted to string object in ISO
        object
        """
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                dict_1[k] = v
        return dict_1
