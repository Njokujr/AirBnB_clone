#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.
    Attributes:
        place_id (str): Public class attribute for Review's place_id
        user_id (str): Public class attribute for Review's user_id
        text (str): Public class attribute for Review's text
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """init method for Review class
        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
