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
           can't ccheck if obj is an instance of BaseModel since
           where basemodel is defined, it imports this module
       """

       key = f"{obj.__class__.__name__}.{obj.id}"
       self.__objects[key] = obj

    def save(self):
        """ It serializes the __objects dict to the json file
        """

        with open(self.__file_path, mode='w+') as fildes:
            my_dict = {}
            for key, value in self.__objects.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, fildes)

    def reload(self):
        """ Deserializes the json file
        """

        try:
            with open(self.__file_path, 'r', encoding="utf-8") as fildes:
                new_dict = json.load(fildes)
                for obj in new_dict.values():
                    self.new(eval(obj["__class__"])(**obj))
        except:
            return
