#!usr/bin/python3

""" Module to serialize the dictionary representation of a file to json format
The serialization flow is as follows:
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -><class 'str'>
 -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """ A class that serializes objects to a json file
        It also deserializes json files to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """

        self.objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
        return (self.__objects)

    def save(self):
        """
           serializes the dictionary __objects to the json file
        """
        with open(self.__file_path, mode='w') as fildes:
            stored_dict = {}
            for k, v in self.__objects.items():
                stored_dict[k] = v.to_dict()
                json.dump(stored_dict, fildes)
        return (self.__file_path)

    def reload(self):
        """
        dESRIALIZES THE JSON file to __objects
        if only it exists
        """

        try:
            with open(self.__file_path, encoding='utf-8') as fildes:
                for obj in json.load(fildes).values():
                    self.new(eval(obj['__class__'])(**obj))
        except FileNotFoundError:
            return
