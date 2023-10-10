#!/usr/bin/python3

import cmd
import sys

class MyConsole(cmd.Cmd):
    intro = "(hbnb)\n\nDocumented commands (type help <topic>):\n========================================\nEOF  help  quit\n"

    def do_EOF(self, arg):
        print("Exiting the console.")
        return True

    def do_help(self, arg):
        if arg:
            print(f"Help for {arg} goes here.")
        else:
            print("Available commands: EOF  help  quit")

    def do_quit(self, arg):
        #print("Exiting the console.")
        return True

    def emptyline(arg):
        pass

if __name__  == "__main__":\
    MyConsole().cmdloop()
