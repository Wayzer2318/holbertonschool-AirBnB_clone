#!usr/bin/python3
import uuid
from datetime import datetime


class BaseModel():
    """
    base model class
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)
        else:
            id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

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

    def to_dict(self):
        """
        to dict
        """
        dic = {}
        dic[__class__] = self.__class__.__name__
        for x, y in self.__dict__.items():
            if isinsinstance(y, datetime):
                dict[x] = y.isoformat()
            else:
                dict[x] = y
        return dic
