#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """City class inherits from BaseModel
    Attributes:
        name (str): Public class attribute for City's name
        state_id (str): Public class attribute for City's state_id
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """init method for City class
        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
