#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

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
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

            class_name = args[0]
            classes_dict = {'BaseModel': BaseModel}
            if class_name not in classes_dict:
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
        if class_name not in storage.classes():
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
        classes_dict = {'BaseModel': BaseModel}
        if class_name not in classes_dict:
            print("** class doesn't exist **")
            return

        print([str(obj) for key, obj in instances.items() if key.startswith(class_name)])

    def do_update(self, arg):
        """
        Updates instance based on class name and id by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
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
        except:
            print("** value missing **")
            return

        obj = storage.all()[key]
        setattr(obj, attribute_name, attribute_value)
        storage.save()
    def classes(self):
        """
        Return a dictionary containing class names as keys and classes as values.
        """
        return {
            'BaseModel': BaseModel,
            'User': User,
            }

if __name__ == '__main__':
    HBNBCommand().cmdloop()

