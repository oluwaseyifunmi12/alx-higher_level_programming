#!/usr/bin/python3
"""Definning a Base class"""
import json


class Base:
    """A base class from which other classes inherits

    Private instance attribute:
        __nb_objects(int) = number of bases created
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing base class

        Args:
            id(int) = identity of each base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances inheriting from Base.

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]))
