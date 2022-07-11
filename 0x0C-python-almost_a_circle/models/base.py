#!/usr/bin/python3
"""Defines a base model class."""

import json
import turtle
import os
import csv


class Base():
    """Represent the base model.
    Represents the 'base' for every other classes in project 0x0C*.
    
    Attributes:
        __nb_objects (int): The number of instantiated bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base:
        
        Args:
            id (int): The identity of the new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of list of dictionaries
        """

        if list_dictionaries is None or list_dictionaries is " ":
            return []
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
