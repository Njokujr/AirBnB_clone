#!/usr/bin/env python3
"""user module, containing User class that inherits
from BaseModel class."""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that extends from BaseModel with the
    following public class attributes.
    + ``email``: string - empty string
    + ``password``: string - empty string
    + ``first_name``: string - empty string
    + ``last_name``: string - empty string
    """
    email = str()
    password = str()
    first_name = str()
    last_name = str()