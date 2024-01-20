#!/usr/bin/python3
"""
Class FileStorage
"""
import json
import uuid
from datetime import datetime
from models.user import User
from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage:
    """
    class FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        objects = {}
        for key, obj in FileStorage.__objects.items():
            objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(objects, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)

                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'BaseModel':
                        class_obj = BaseModel
                    elif class_name == 'User':
                        class_obj = User
                    elif class_name == 'Place':
                        class_obj = Place
                    elif class_name == 'State':
                        class_obj = State
                    elif class_name == 'Review':
                        class_obj = Review
                    elif class_name == 'Amenity':
                        class_obj = Amenity
                    elif class_name == 'City':
                        class_obj = City
                    else:
                        pass

                    obj_instance = class_obj(**value)
                    FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
