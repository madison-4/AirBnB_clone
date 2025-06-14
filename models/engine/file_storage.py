#!/usr/bin/python3
""" It serializes isntances to json files
it also deserializes them
"""

import json

class FileStorage():
    """This class serializes anmd deserialies
    instances to a json file and deserilizes json files to instances
    """

    __file_path = savefile.json
    __objects = {}
    def __init__(self):
        """ Instantiates the class with its variables
        and attribiutes
        """

        def all(self):
            """ Returns the objects dictionary
            """

            return __objects

        def new(self, obj):
            """ It sets in the __objects an obj with the key classname.id
            """

             key = f"{obj.__class__.__name__}"
             self.__objects[key] = obj

        def save(self):
            """ It serializes the __objects dict to the json file
            """


            with open(self.__file_path, mode='w+') as fildes:
                json.dump(self.__objects, self.__file_path)

        def reload(self):
            """ Deserializes the json file
            """
            
