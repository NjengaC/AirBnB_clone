#!/usr/bin/python3
"""A class review"""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """Defining a class Review"""
    place_id = ""
    user_id = ""
    text = ""
