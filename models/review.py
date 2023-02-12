#!/usr/bin/env python3
"""
Script containing defination of Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines the class City with the following list of
    class attributes:
    + `place_id`: string - empty string: it will be the Place.id
    + `user_id`: string - empty string: it will be the User.id
    + `text`: string - empty string
    """

    place_id = str()
    user_id = str()
    text = str()
