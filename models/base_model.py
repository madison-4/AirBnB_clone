#!/usr/bin/python3
""" A module to define all common attri9butes and methods
    This is the root class that all other classess in this project inherit from
The attributes and methods are common to all other classes
"""


from uuid import uuid4
from datetime import datetime


class (BaseModel):
    """Public instance attributes:
        id: string - assign with an uuid when an instance is created:
          you can use uuid.uuid4() to generate unique id a string
           the goal is to have unique id for each BaseModel
        created_at: datetime - assign with the current datetime when an
        instance is created
        updated_at: datetime - assign with the current datetime when an instance
            is created and it will be updated every time you change your object
    """
    def __str__(self):
        """ This method aims to print
        [<class name>] (<self.id>) <self.__dict__>
        each tiem it is called
        """

        name = f"[{type(self).__name__}] ({self.id}) {self.id}"
        return (name)

    def save(self):
        """ A function to uodate the instance attribute
            update_at to current time
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the
           instance
        """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "update_at"):
                v = self.__dict__[k].isoformat()
                my_dict[k] = v
        return my_dict
