!/usr/bin/python3
import uuid
import datetime


"""
create base model
"""
class BaseModel():
    def __init__(self):
        id = str(uuid.uuid4())
        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()

    def __str__(self):
        """
        __str__
        """
        print("{} {} {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        save
        """
        self.updated_at = datetime.datetime.now()
    
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
