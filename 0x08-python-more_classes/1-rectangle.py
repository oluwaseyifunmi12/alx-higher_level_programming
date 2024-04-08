#!/usr/bin/python3
""" Defines a new Rectangle class"""


class Rectangle:
    """ A rectangle class"""

    def __init__(self, width = 0, height = 0):
        """
        initializes the class
        Args:
            height(int): the height of the rectangle
            width(int): the width of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Gets the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value    

    @property
    def height(self):
        """ Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
