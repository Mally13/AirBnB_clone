#!/usr/bin/python3

"""Import statements from the modules"""
import cmd
import shlex
import sys
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.state import State
from models import storage

"""a dictionary that maps class names (strings)
to their corresponding class objects"""

valid_classes = {
    'BaseModel': BaseModel,
    'City': City,
    'State': State,
    'Review': Review,
    'Place': Place,
    'User': User,
    'Amenity': Amenity
}


class HBNBCommand(cmd.Cmd):
    """
    main class that defines the HBnB command intepreter
    """
    prompt = "(hbnb) "

    def default(self, arg):
        """
        Called for unknown commands eg. do_all
        """
        if '.' in arg:
            class_name, command = arg.split('.')
            if command == 'all()':
                self.do_all(class_name)
                return
            elif class_name in valid_classes and command == 'count()':
                self.count(class_name)
                return
            elif (command.startswith('show(') and
                  command.endswith(')')):
                instance_id = command[5:-1]
                self.do_show(class_name + ' ' + instance_id)
                return
            elif (command.startswith('destroy(') and
                  command.endswith(')')):
                instance_id = command[8:-1]
                self.do_destroy(class_name + ' ' + instance_id)
                return
            elif (command.startswith('update(') and
                  command.endswith(')')):
                args = command[7:-1].split(',')
                instance_id = args[0].strip()
                attr_name = args[1].strip()
                attr_value = args[2].strip()
                var = (f"{class_name} {instance_id} {attr_name} {attr_value}")
                self.do_update(var)
                return
        print("*** Unknown syntax: {}".format(arg))
        return False

    def emptyline(self):
        """This method does nothing in case of an empty input"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        args = shlex.split(arg)
        if (len(args) < 1):
            print("** class name missing **")
        elif (args[0] in valid_classes):
            new = valid_classes[args[0]]()
            new.save()
            print("{}".format(new.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id."""
        all_objects = storage.all()
        args = shlex.split(arg)
        if (len(args) < 1):
            print("** class name missing **")
        elif (args[0] not in valid_classes):
            print("** class doesn't exist **")
        elif (len(args) < 2):
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            if obj_key in all_objects:
                print("{}".format(all_objects[obj_key]))
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        all_objects = storage.all()
        args = shlex.split(arg)
        if (len(args) < 1):
            print("** class name missing **")
        elif (args[0] not in valid_classes):
            print("** class doesn't exist **")
        elif (len(args) < 2):
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            if obj_key in all_objects:
                all_objects.pop(obj_key)
                storage.__objects = all_objects
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of
        all instances based or not on the class name.
        """
        all_objects = storage.all()
        args = shlex.split(arg)
        output_list = []
        if (len(args) < 1):
            for key, value in all_objects.items():
                output_list.append(str(value))
        elif (args[0] not in valid_classes):
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            filtered_objects = {key:
                                value for key,
                                value in all_objects.items()
                                if class_name in key
                                }
            for key, value in filtered_objects.items():
                output_list.append(str(value))
        if len(output_list) != 0:
            print(output_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute and also saves the updated instance to JSON file"""
        all_objects = storage.all()
        args = shlex.split(arg)
        if (len(args) < 1):
            print("** class name missing **")
        elif (args[0] not in valid_classes):
            print("** class doesn't exist **")
        elif (len(args) < 2):
            print("** instance id missing **")
        elif (len(args) < 3):
            print("** attribute name missing **")
        elif (len(args) < 4):
            print("** value missing **")
        else:
            obj_key = args[0] + "." + args[1]
            if obj_key in all_objects:
                instance = all_objects[obj_key]
                instance_attr = args[2]
                instance_val = args[3]
                cant_update = ["id", "created_at", "updated_at"]
                if instance_attr not in cant_update and hasattr(
                        instance, instance_attr):
                    attr_type = type(getattr(instance, instance_attr))
                    try:
                        setattr(instance, instance_attr, attr_type(
                            instance_val))
                        instance.save()
                    except ValueError:
                        return
            else:
                print("** no instance found **")

<<<<<<< HEAD
    def do_show(self, arg):
        """shows the objects"""
        return False
=======
    def count(self, arg):
        """
        Retrieves the number of instances of a class
        """
        class_list = []
        all_objects = storage.all()
        class_name = arg
        filtered_objects = {key:
                            value for key,
                            value in all_objects.items()
                            if class_name in key
                            }
        for key, value in filtered_objects.items():
            class_list.append(str(value))
        print(len(class_list))
>>>>>>> main

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Handles EOF signal to exit the program
        """
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
