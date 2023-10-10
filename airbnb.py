#!/usr/bin/python3

import cmd
import sys

class MyConsole(cmd.Cmd):
    prompt = "(hbnb) "
    #pass
    def do_create(self, line):
        print("I have created", line)


    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

if __name__  == "__main__":\
    MyConsole().cmdloop()  
