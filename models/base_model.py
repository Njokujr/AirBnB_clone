#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
from datetime import datetime
import uuid
import models


class BaseModel:
    ''' BaseModel class '''
    def __init__(self, *args, **kwargs):
        '''
        initation of basemodel
        Args:
        *args: arguments passed in
        **kwargs: arguments with key values
        Return:
        None
        '''
        if len(kwargs) != 0:
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(self.created_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """str method for BaseModel Class
            Return:
                string (str): string descriptor for BaseModel Class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict_)

    def save(self):
        ''' updates date for updated_at attribute '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' returns dictonary with all key values of instance '''
        mydict = self.__dict__.copy()
        mydict['__class__'] = self.__class__.__name__
        mydict['created_at'] = self.created_at.isoformat()
        mydict['updated_at'] = self.updated_at.isoformat()

        return mydict
