#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    Defines the HBnB command intepreter
    """
    prompt = "(hbnb) "

    def default(self, arg):
        """
        Called for unknown commands
        """
        print("*** Unknown syntax: {}".format(arg))
        return False

    def emptyline(self):
        """Does nothing in case of an empty input"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        valid_classes = {
            'BaseModel': BaseModel,
            'City': City,
            'State': State,
            'Review': Review,
            'Place': Place,
            'User': User,
            'Amenity': Amenity
        }
        args = arg.split()
        if (len(args) < 1):
             print("** class name missing **")
        elif (args[0] in valid_classes):
             new = valid_classes[args[0]]()
             new.save()
             print("{}".format(new.id))
        else:
             print("** class doesn't exist **")         

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handles EOF signal to exit the program"""
        print("")
        return True


if __name__ == "__main__":
        HBNBCommand().cmdloop()
