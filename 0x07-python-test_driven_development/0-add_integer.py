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
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
