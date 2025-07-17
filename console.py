#!/usr/bin/python3
""" A module that makes a simple command line interpreter
"""

import models
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
    storage = models.storage

    def do_EOF(self, line):
        """ Exits the interorter gracefully
        """

        return True

    @staticmethod
    def classcheck(line):
        """ A function to check that the given class exists
        Args:
             line: The class name to check and rint
        Return:
             True if the class exists and false otherwise
        """

        comms = line.split()
        name = comms[0]
        if name not in (HBNBCommand.classes):
            print(HBNBCommand.nexist)
            return False
        else:
            return True

    def do_quit(self, line):
        """Quits the interprter
        if line exists it willuse it as the
        exit status
        """

        if line:
            try:
                line = int(line)
                if (type(line) is int):
                    sys.exit(line)
            except:
                return True
        return True

    def help_quit(self):
        """ lists how to use the quit command
        """

        print(f"quit [status]")
        print("quits the interpreter with [status] is status is a valid int")

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

    def do_show(self, line):
        """ A function to show the string rep of an instance
        """

        if not line:
            print(self.miss)
        if not (self.classcheck(line)):
            pass
        else:
            comms = line.split()
            if (len(comms) != 2):
                print("** instance id missing **")
            else:
                key = f"{comms[0]}.{comms[1]}"
                if key not in self.storage.all():
                    print("** no instance found **")
                else:
                    print(self.storage.all()[key])

    def do_destroy(self, line):
        """ A function to delete instances of an id and save the changes
        """

        if not line:
            print(self.miss)
        if not (self.classcheck(line)):
            pass
        else:
            comms = line.split()
            if (len(comms) != 2):
                print("**instance id missing **")
            else:
                key = f"{comms[0]}.{comms[1]}"
                if key not in self.storage.all():
                    print("** no instance found **")
                else:
                    del self.storage.all()[key]
                    self.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
