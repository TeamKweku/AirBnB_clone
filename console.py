#!/usr/bin/python3
"""a module that implements the console app (cmd)"""
import cmd


class HBNBCommand(cmd.Cmd):
    """the class that handles the cmd console interface"""

    prompt = "(hbnb) "

    def do_quit(self):
        """method to exit the program if quit is used"""
        return True

    def do_EOF(self):
        """method to exit the program with EOF"""
        return True

    def emptyline(self):
        """an emptyline should do nothing"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
