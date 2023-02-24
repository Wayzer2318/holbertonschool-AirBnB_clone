#!/usr/bin/python3
""" airbnb clone console program """
import sys
import cmd
import models


from models.base_model import BaseMods
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ HBNB command class """
    prompt = '(hbnb) '
    class_dict = {"BaseModel": BaseModel, "User": User}

    def do_create(self, args):
        """ create instance """
        if not args:
            print("** class name missing **")
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

    def do_update(self, args):
        """ Update an instance """
        strings = args.split()
        models.storage.reload()
        new_dict = models.storage.all()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        elif strings[0] + '.' + strings[1] not in new_dict.keys():
            print("** no instance found **")
        elif len(strings) == 2:
            print("** attribute name missing **")
        elif len(strings) == 3:
            print("** value missing **")
        else:
            key = strings[0] + '.' + strings[1]
            if hasattr(new_dict[key], strings[2]):
                caster = type(getattr(new_dict[key], strings[2]))
                setattr(new_dict[key], strings[2], caster(strings[3]))
                models.storage.save()
            else:
                setattr(new_dict[key], strings[2], strings[3])
                models.storage.save()

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
