#!/usr/bin/python3
""" A function to for sub classes"""


def inherits_from(obj, a_class):
    """
    Checks if the object is exactly a subclass of the specified class.

    Args:
    - obj: The object to check
    - a_class: The class to compare against

    Returns:
    - bool: True if obj is exactly an instance of a_class, False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
