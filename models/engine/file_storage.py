#!/usr/bin/python3
""" It serializes isntances to json files
it also deserializes them
"""

import json

class FileStorage():
    """This class serializes anmd deserialies
    instances to a json file and deserilizes json files to instances
    """

    __file_path = 'file.json'
    __objects = {}
    def __init__(self):
        """ Instantiates the class with its variables
        and attribiutes
        """

    def all(self):
        """ Returns the objects dictionary
        """

        return self.__objects

    def new(self, obj):
       """ It sets in the __objects an obj with the key classname.id
           Use with caution since it does not check if the
            function does not check the passed object is of the BaseModel class
       """

#       if not (isinstance(obj, BaseModel)):
#       """I wanted to check if it's a basemodel class however
#         I can't import the basemodel class since it'll create a circular import
#         i.e. The base model class imports this class
#           return
       key = f"{obj.__class__.__name__}.{obj.id}"
       self.__objects[key] = obj.to_dict()

    def save(self):
        """ It serializes the __objects dict to the json file
        """

        with open(self.__file_path, mode='w+') as fildes:
            json.dump(self.__objects, fildes)

    def reload(self):
        """ Deserializes the json file
        """

        try:
            with open(self.__file_path, 'r') as fildes:
                temp = json.load(fildes)
                self.__objects.update(temp)
        except:
                pass
