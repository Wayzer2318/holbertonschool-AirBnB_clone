#!/usr/bin/python3
""" base model """
import uuid
import datetime


import models


class BaseModel:
    """ base model class """

    def __init__(self, *args, **kwargs):
        if kwargs:
            created_at = datetime.datetime.strptime(
                kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            updated_at = datetime.datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["created_at"] = created_at
            kwargs["updated_at"] = updated_at

            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

            models.storage.new(self)

    def __str__(self):
        r = [
            '[%s]' % (self.__class__.__name__),
            '(%s)' % (self.id),
            '%s' % (self.__dict__),
        ]

        return ' '.join(r)

    def save(self):
        self.updated_at = datetime.datetime.now()

        models.storage.save()

    def to_dict(self):
        new_dict = dict(self.__dict__)

        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
