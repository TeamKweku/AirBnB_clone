#!/usr/bin/python3
"""a module that implements the console app (cmd)"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """the class that handles the cmd console interface"""

    prompt = "(hbnb) "

    # stores available classes in key, value pair (dict)
    available_cls = {
        "BaseModel": BaseModel,
    }

    def do_quit(self, line):
        """method to exit the program if quit is used"""
        return True

    def do_EOF(self, line):
        """method to exit the program with EOF"""
        return True

    def emptyline(self):
        """an emptyline should do nothing"""
        pass

    def do_create(self, lines):
        """creates a new instance.
        Usage: create <class_name>
        """
        if not lines:
            print("** class name missing **")
            return

        tokens = shlex.split(lines)
        # print(len(tokens))
        if len(tokens) == 1:
            if tokens[0] not in HBNBCommand.available_cls.keys():
                print("** class doesn't exist **")
                return

            # print("available")
            obj = HBNBCommand.available_cls[tokens[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, lines):
        """prints the string representation of an instance based on the
        class name and id

        Usage: show <class_name> <object_id>
        """
        if not lines:
            print("** class name missing **")
            return
        tokens = shlex.split(lines)
        if tokens[0] not in HBNBCommand.available_cls.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) == 1:
            print("** instance id missing **")
            return
        if len(tokens) == 2:
            # load the dict format of objects from file storage
            storage.reload()

            # return all ojects
            objs = storage.all()

            key = f"{tokens[0]}.{tokens[1]}"
            if key not in objs.keys():
                print("** no instance found **")
                return
            else:
                print(objs[key])

    def do_destroy(self, lines):
        """Deletes an instance based on the class name and id

        Usage: destroy <class_name> <object_id>
        """
        if not lines:
            print("** class name missing **")
            return
        tokens = shlex.split(lines)
        if tokens[0] not in HBNBCommand.available_cls.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) == 1:
            print("** instance id missing **")
            return
        if len(tokens) == 2:
            # load the dict format of objects from file storage
            storage.reload()

            # return all ojects
            objs = storage.all()

            key = f"{tokens[0]}.{tokens[1]}"
            if key not in objs.keys():
                print("** no instance found **")
                return
            else:
                del objs[key]

            # save change into the JSON file
            storage.save()

    def do_all(self, lines):
        """Prints all string representation of all instances
        Usage: all or all <class_name>
        """
        objs = storage.all()

        # no class name passed to all $ all
        if not lines:
            obj_list = []
            for key in objs:
                obj_list.append(str(objs[key]))
            print(obj_list)
            return

        # if a class name passed to $ all <class_name>
        tokens = shlex.split(lines)

        if tokens[0] not in HBNBCommand.available_cls.keys():
            print("** class doesn't exist **")

        else:
            print([str(objs[key]) for key in objs if key.split(".")[0] == tokens[0]])

            return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
