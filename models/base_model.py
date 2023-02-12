#!/usr/bin/env python3
"""
Defines the class BaseModel being the first
piece of the serialization/deserialization process.
"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
    Defines all common attributes/methods
    for other classes. This class will be the first
    piece of the serialization/deserialization process.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the instance attributes.
        """

        if len(kwargs) != 0:
            kwargs.pop("__class__", None)
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    # basic class methods
    def __str__(self):
        """
        Return the string representation of an object.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at atrr with the current datetime,
        and then call on the storage save method to update
        database.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__.
        """
        _dict = {"__class__": self.__class__.__name__}
        _dict.update(self.__dict__)
        _dict["created_at"] = self.created_at.isoformat()
        _dict["updated_at"] = self.updated_at.isoformat()
        return _dict
