#!/usr/bin/python3
import models
import uuid
from datetime import datetime
"""
Module initialises the baseodel with requirements as shown
"""
#formats = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    class BaseModel from which objs will inherit from
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor for BaseModel
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    setattr(self, key, value)
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                elif key == '__class__':
                    pass
                else:
                    setattr(self, key, value)


    def __str__(self):
        """
        String repr of BaseModel
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        """
         update the pub instance attr updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dict containing all keys/values of __dict__ of the instance.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict
