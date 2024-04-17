#!/usr/bin/python3
"""Defines a function to writes to text files."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        char_count = f.write(text)
        return char_count
