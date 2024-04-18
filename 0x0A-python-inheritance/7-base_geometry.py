#!/usr/bin/python3
"""Defines a Base Geometry class."""


class BaseGeometry:
    """Represents a geometry class"""
    def area(self):
        """A area public instance that raises an exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        An integer validator instance
        Args:
            name(str): string to be validated
            value(int): the checking point
        Raises:
            TypeError: when value is not of type int
            ValuError: when value is less than or equal to 0
        Returns:
            Nothing
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
