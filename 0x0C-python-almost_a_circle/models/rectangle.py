#!/usr/bin/python3
"""Defining a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle class

        Args:
            width(int): width of the rectangle
            height(int):  height of the rectangle
            x(int): the x coordinate of the rectangle
            y(int): the y coordinate of the rectangle
            id(int): the identity of the instance of rectangle

        Raises:
            TypeError: if inputs are not integers
            ValueError: if width or height is less than or equal 0
            ValueError: if x or y is less than 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x coordinate of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y coordinate of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """defines the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """displays the rectangle with # character"""
        for lines in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """A string form of the rectangle details"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.x, self.y, self.width, self.height))
