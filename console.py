#!/usr/bin/python3
""" A module that makes a simple command line interpreter
"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """A commandline interpreter to test the AirBnB
    console.
    """

    prompt = '(hbnb) '

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

    def do_create(self, line):
        """ Create an object of a given class
        """

        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
