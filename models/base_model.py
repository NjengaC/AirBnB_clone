#!/usr/bin/python3
import models
import uuid
from datetime import datetime

"""
Module initialises the baseodel with requirements as shown
"""


class BaseModel:
    """
    class BaseModel from which objs will inherit from
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor for BaseModel
        """
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        String repr of BaseModel
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
         update the pub instance attr updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Returns a dict containing all keys/values of __dict__ of the instance.
        """
        instance_dict = self.__dict__.copy()

        instance_dict.update({'__class__': self.__class__.__name__,
                              'created_at': self.created_at.isoformat(),
                              'updated_at': self.updated_at.isoformat(),
                              })
        return instance_dict
