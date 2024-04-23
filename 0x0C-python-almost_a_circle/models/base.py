#!/usr/bin/python3
"""Definning a Base class"""


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
