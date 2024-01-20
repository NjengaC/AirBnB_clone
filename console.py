#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
import sys
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    classes_dict = {"BaseModel": BaseModel, "User": User,
                  "Place": Place, "State": State,
                  "City": City, "Amenity": Amenity,
                  "Review": Review}

    def default(self, line):
        """
        Default behavior for unrecognized commands. Handle <class name>.all()
        """
        if line.endswith(".all()"):
            class_name = line.split(".")[0]
            if class_name in self.classes_dict:
                print([str(obj) for obj in storage.all().values()
                      if isinstance(obj, self.classes_dict[class_name])])
            else:
                print("** class doesn't exist **")
        elif line.endswith(".count()"):
            class_name = line.split(".")[0]
            if class_name in self.classes_dict:
                count = sum(1 for obj in storage.all().values()
                            if isinstance(obj, self.classes_dict[class_name]))
                print(count)
            else:
                print("** class doesn't exist **")
        else:
            print(f"Unknown syntax: {line}")

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty input line
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string repr of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return

        class_name = args[0]
        if not class_name or class_name not in self.classes_dict:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]

        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if not class_name or class_name not in self.classes_dict:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string repr of all instances based or not on the class name.
        Usage: all [class name]
        """
        args = arg.split()
        instances = storage.all()

        if not args:
            print([str(obj) for obj in instances.values()])
            return

        class_name = args[0]

        if class_name not in self.classes_dict:
            if '.' in class_name and class_name.split('.')[1] == 'all()':
                class_name = class_name.split('.')[0]
                if class_name in classes_dict:
                    print([str(obj) for obj in models.storage.all().values()
                          if isinstance(obj, classes_dict[class_name])])
                else:
                    print("** class doesn't exist **")
            else:
                print("** class doesn't exist **")
            return

        print([str(obj) for key, obj in
              instances.items() if key.startswith(class_name)])


    def do_update(self, arg):
        """
        Updates instance based on class name and id by adding or updating attr
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes_dict:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value_str = args[3]
        try:
            attribute_value = eval(attribute_value_str)
        except Exception:
            print("** value missing **")
            return

        obj = storage.all()[key]
        setattr(obj, attribute_name, attribute_value)
        storage.save()
        
    def preloop(self):
        """
        Prints the prompt only if isatty is false
        """
        if not sys.__stdin__.isatty():
            print("(hbnb)")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
