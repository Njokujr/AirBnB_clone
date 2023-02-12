#!/usr/bin/python3
"""
The console prompt command
"""

import cmd
import re
import shlex
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from datetime import datetime
from ast import literal_eval
import functools
from shlex import split
from models.engine import *


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """Implementing cmd module that quits out of the interpreter when
    the user types quit or EOF.
    """

    prompt = "(hbnb)"

    def precmd (self, line):
        """Intercepts commands to test for class.syntax()"""
        # print("PRECMD:::", line)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def do_EOF(self, line):
        """command to exit the console"""
        print("")
        return True

    def emptyline(self):
        """when line is empty do nothing"""
        return False

    def do_create(self, inp):
        """creates a new class instance"""
        arguments = inp.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return False
        if arguments[0] in classes:
            object = classes[arguments[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(object.id)
        object.save()

    def do_show(self, inp):
        """shows string rep of an instance
        class name and id
        """

        arguments = inp.split()
        models.storage.reload()
        if len(arguments) == 0:
            print("** class name missing **")
            return False
        if arguments[0] in classes:
            if len(arguments) > 1:
                keys = arguments[0] + "." + arguments[1]
                if keys in models.storage.all():
                    print(models.storage.all()[keys])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, inp):
        """deletes an instance based on class/id"""
        arguments = inp.split()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] in classes:
            if len(arguments) > 1:
                keys = arguments[0] + "." + arguments[1]
                if keys in models.storage.all():
                    models.storage.all().pop(keys)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, inp):
        """prints all instances if they exist"""
        arguments = inp.split()
        models.storage.reload()
        instance_list = []
        if len(arguments) == 0:
            for v in models.storage.all().values():
                instance_list.append(str(v))
            print("[", end="")
            print(", ".join(instance_list), end="")
            print("]")
        elif arguments[0] in classes:
            for keys in models.storage.all():
                if arguments[0] in keys:
                    instance_list.append(str(models.storage.all()[keys]))
            print("[", end="")
            print(", ".join(instance_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, inp):
        """ update an instance based on its UUID """
        models.storage.reload()
        if len(inp) == 0:
            print("** class name missing **")
            return
        else:
            ac = shlex.split(inp)
            if ac[0] not in classes:
                print("** class doesn't exist **")
                return
            if ac[0] in classes and len(ac) < 2:
                print("** instance id missing **")
                return
            tmp = ac[0] + '.' + ac[1]
            if tmp in models.storage.all():
                to_update = models.storage.all()[tmp].__dict__
                if len(ac) < 3:
                    print("** attribute name missing **")
                elif len(ac) < 4:
                    print("** value missing **")
                else:
                    key = ac[2]
                    try:
                        attr = type(to_update[key])
                        value = attr(ac[3])
                    except KeyError:
                        value = ac[3]
                    to_update[key] = value
                    models.storage.save()
            else:
                print("** no instance found **")
     #################
    # Help Functions#
    #################

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("CTRL + D (EOF) to exit the program")

    def help_create(self):
        print("Usage: create <valid class name>")

    def help_show(self):
        print("Usage: show <valid class name> <valid id>")

    def help_destroy(self):
        print("Usage: destroy <valid class name> <valid id>")

    def help_all(self):
        print("Usage: all OR all <valid class name>")

    def help_update(self):
        print("Usage: update <valid class name>", end="")
        print("<valid id> <attribute name> <attribute value>")


if __name__ == '__main__':
        HBNBCommand().cmdloop()
