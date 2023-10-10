#!/usr/bin/python3

import cmd
import sys
import uuid
from datetime import datetime

class MyConsole(cmd.Cmd):
    prompt = "(hbnb) "
    #pass
    """def do_help(self, arg):
        if arg:
            print(f"Help for {arg} goes here.")
        else:
            print("Available commands: EOF  help  quit")"""

    def do_create(self, line):
        print("I have created", line)

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        #print("Exiting the console.")
        return True

if __name__  == "__main__":\
    MyConsole().cmdloop()  
