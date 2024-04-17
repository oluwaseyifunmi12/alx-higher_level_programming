#!/usr/bin/python3
"""Defines a function to append text to text files."""


def write_file(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended. The number of characters written.
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        char_count = f.write(text)
        return char_count
