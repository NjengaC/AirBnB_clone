# models/user.py
"""
Class User
"""
from models.base_model import BaseModel
import models


class User(BaseModel):
    """
    User class that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    storage.new(self)
