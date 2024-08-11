#!/usr/bin/python3
""" A module to implement the entry point of the command interporeter
"""


import cmd
import re


class HBNBCommand(cmd.Cmd):
    """ A class to define the console part of the airbnb clone
    """

    prompt = "(hbnb)"
    storage = models.storage

    def emptyline(self):
        """ What to execute when an empty line and Enter
            id pressed
        """

        pass

    def default(self, arg):
        """ Deafukt beahviour for invalid input
        """

        print("*** Unknown syntax: {arg}")
        return False
    
