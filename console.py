#!/usr/bin/python3

import cmd
import sys

class HbnbConsole(cmd.Cmd):
    """
    Defines the HBnB command intepreter
    """
    prompt = "(hbnb) "

    def default(self, line):
        """
        Called for unknown commands
        """
        if not line.strip():
            pass
        else:
            print("*** Unknown syntax: {}".format(line))

    def emptyline(self):
        """Does nothing in case of an empty input"""
        pass

    def do_create(self, line):
        print("I have created", line)

    def do_quit(self, line):
        return True

if __name__  == "__main__":
    try:
        HbnbConsole().cmdloop()  
    except KeyboardInterrupt:
        print("\n Exiting...")