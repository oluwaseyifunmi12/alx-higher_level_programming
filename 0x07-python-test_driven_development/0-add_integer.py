#!/usr/bin/python3
""" A function to add two numbers"""


def add_integer(a, b=98):
    """ This function accepts two integers
        Raises:
            TypeError: if a or b is a non-integer or non-float.
        Both values should be typecated into int before addition
        Returns:
            the value of addition of both numbers
    """
    if not all(isinstance(var, (int, float)) for var in (a, b)):
        raise TypeError(" {} must be an integer".format(
            'a' if not isinstance(a, (int, float)) else 'b'))

    a = int(a)
    b = int(b)

    return (a + b)
