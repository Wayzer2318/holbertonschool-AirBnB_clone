#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base class
    """
    def __init__(self, *args, **kwargs):
        """
        baseModel
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    dtob = datetime.strptime(v,
                                                  '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, k, dtob)
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        string representation
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary
        """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for l, j in self.__dict__.items():
            if isinstance(j, datetime):
                dic[l] = j.isoformat()
            else:
                dic[l] = j
        return dic
