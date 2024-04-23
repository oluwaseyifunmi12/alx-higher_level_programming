#!/usr/bin/python3
"""Defines a sub class of rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square class

        Args:
            size(int): shows the size of the square
            x(int): x coordinate of the square
            y(int): y coordinate of the square
            id(int): identity of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """A string representation of the square details"""
        return "[Square] ({}) {}/{} - {}".
    format(self.id, self.x, self.y, self.width or self.height)

    @property
    def size(self):
        """Gets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the value of the square"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """A dictionary representation of the square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
