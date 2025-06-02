#!/usr/bin/python3
""" It serializes isntances to json files
it also deserializes them
"""

class FileStorage():
    """This class serializes anmd deserialies
    instances to a json file and deserilizes json files to instances
    """

    def __init__(self):
        """ Instantiates the class with its variables
        and attribiutes
        """

        self.__file_path
