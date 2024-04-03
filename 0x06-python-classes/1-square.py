#!/usr/bin/python3
"""Another square class with a size attribute"""


class Square:
    """square class attributes details
    Attributes:
        __size (int): gives the info on the size of a side
    """
    def __init__(self, size):
        """initialization process
        Args:
            size (int): gives the info on the size of a side
        Returns: none
        """
        self.__size = size
