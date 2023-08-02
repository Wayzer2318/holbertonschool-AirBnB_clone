#!/usr/bin/python3
""" airbnb clone console program """
import cmd
import models
from models.user import User
from models.base_model import BaseModel
import sys


class HBNBCommand(cmd.Cmd):
    """ HBNB command class """
    prompt = '(hbnb) '
    class_dict = {"BaseModel": BaseModel, "User": User}

    def do_create(self, args):
        """ create instance """
        if not args:
            print("** class name messing **")
        else:
            if args in HBNBCommand.class_dict.keys():
                new_instance = HBNBCommand.class_dict[args]()
                models.storage.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """ print string od instance """
        strings = args.split()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        else:
            key_value = strings[0] + '.' + strings[1]
            try:
                print(models.storage.all()[key_value])
            except KeyError:
                print("** no instance found **")

    def do_all(self, args):
        """ print string of all instance or just a class """
        strings = args.split()
        new_list = []
        address_value = 0
        if len(strings) == 1:
            if strings[0] not in HBNBCommand.class_dict.keys():
                print("** class doesn't exist **")
            else:
                for key in models.storage.all().keys():
                    class_name = key.split('.')
                    if class_name[0] == strings[0]:
                        new_list.append(str(models.storage.all()[key]))
                    else:
                        continue
                print(new_list)
        else:
            for key, value in models.storage.all().items():
                new_list.append(str(models.storage.all()[key]))
            print(new_list)

    def do_destroy(self, args):
        """ delete an instance """
        strings = args.split()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        else:
            key_value = strings[0] + '.' + strings[1]
            try:
                del models.storage.all()[key_value]
                models.storage.save()
            except KeyError:
                print("** no instance found **")

    def emptyline(self):
        """ handle empty line """
        pass

    def do_EOF(self, arg):
        """ handle EOF """
        return True

    def do_quit(self, arg):
        """ handle quit """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
