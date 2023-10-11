#!/usr/bin/python3

import cmd
import sys


class HbnbConsole(cmd.Cmd):
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
        """Creates an object"""
        print("I have created", arg)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handles EOF signal to exit the program"""
        print("")
        return True


if __name__ == "__main__":
    try:
        HbnbConsole().cmdloop()
    except KeyboardInterrupt:
        print("\n Exiting HBnB...")
