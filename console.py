#!/usr/bin/python3
""" A module that makes a simple command line interpreter
"""

import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """A commandline interpreter to test the AirBnB
    console.
    """

    classes = ['BaseModel', 'FileStorage']
    prompt = '(hbnb) '
    nexist= "** class doesn't exist **"
    miss = "** class name missing **"
    
    def do_EOF(self, line):
        """ Exits the interorter gracefully
        """

        return True

    def do_quit(self, line):
        """Quits the interprter
        if line exists it willuse it as the
        exit status
        """

        if line:
            if (type(line) is int):
                sys.exit(line)
        return True

    def emptyline(self):
        """ What to do when an empoty line is encountred
        """

        pass

    def help_quit():
        """The help bar for the quit command
        """
        
        print("quits the interpreter")

    def do_create(self, line):
        """A command to create an object of a class specified by line
        """

        if not line:
            print(self.miss)
        else:
            comms = line.split()
            cla = comms[0]
            if cla not in (self.classes):
                print(self.nexist)
            else:
                obj = eval(cla)()
                obj.save()
        

if __name__ == "__main__":
    HBNBCommand().cmdloop()
