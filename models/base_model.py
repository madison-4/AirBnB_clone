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
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
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

        self.updated_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing the
        key/values of the __dict__ instance
        """

        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        if (type(my_dict['created_at']) is not str):
            my_dict['created_at'] = my_dict['created_at'].isoformat()
        if (type(my_dict['updated_at']) is not str):
            my_dict['updated_at'] = my_dict['updated_at'].isoformat()

        return my_dict
