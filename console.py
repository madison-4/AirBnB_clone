#!/usr/bin/python3
""" A module that makes a simple command line interpreter
"""

import models
import re
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from shlex import split


# A global constant since both functions within and outside uses it.
CLASSES = [
    "BaseModel",
    "User",
    "City",
    "Place",
    "State",
    "Amenity",
    "Review"
]


def parse(arg):
    """ function to strip arguments and m,ake them able to strip functions
    It simply removes nonimportant xchars
    """

    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


def check_args(args):
    """checks if args is valid

    Args:
        args (str): the string containing the arguments passed to a command

    Returns:
        Error message if args is None or not a valid class, else the arguments
    """
    arg_list = parse(args)

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in CLASSES:
        print("** class doesn't exist **")
    else:
        return arg_list


class HBNBCommand(cmd.Cmd):
    """A commandline interpreter to test the AirBnB
    console.
    """

    classes = ['BaseModel', 'FileStorage']
    prompt = '(hbnb) '
    nexist = "** class doesn't exist **"
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
        if comms:
            name = comms[0]
        else:
            return False
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
            except Exception as e:
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
            if cla not in CLASSES:
                print(self.nexist)
            else:
                obj = eval(cla)()
                obj.save()
                print(obj.id)

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

    def help_destroy(self):
        """ documentation on how the destroy function works
        """

        print("The destroy function deletes an object from the program as well\
        as from the file.json storage\
        works like destroy [classname] [object id]\
        If the object exists it will be deleted.\
        If the class or obj is invalid it will say so and do nothing\
        ")

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

    def help_all(self):
        """A function to print the usage for all
        """

        string = """all command prints a list of all instances of a particular\
        class.
        usage all [classname]
        """

    def do_all(self, line):
        """ prints all instances of a class
        """

        arg_list = split(line)
        objects = self.storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                       if arg_list[0] in str(obj)])

    def help_update(self):
        """ update attributes in the object
        """

        pr_str = """This function changes, adds or removes\
        the value of partuicular attributes for an instance\
        Usage: update Class instanceid attribute name attriobute value
        """
        print(pr_str)

    def do_update(self, line):
        """ command to update attribute name
        """

        arg_list = check_args(line)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(arg_list[0], arg_list[1])
                if instance_id in self.storage.all():
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[instance_id]
                        if arg_list[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[arg_list[2]])
                            setattr(obj, arg_list[2], v_type(arg_list[3]))
                        else:
                            setattr(obj, arg_list[2], arg_list[3])
                else:
                    print("** no instance found **")

            self.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
