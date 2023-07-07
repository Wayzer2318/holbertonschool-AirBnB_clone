#!usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    base model class
    """
    def __init__(self, *args, **kwargs):
        """ initialisaation  """
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    timeval = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, timeval)
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        __str__
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        save
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        to dict
        """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, l in self.__dict__.items():
            if isinstance(l, datetime):
                dic[k] = l.isoformat()
            else:
                dic[k] = l
        return dic
