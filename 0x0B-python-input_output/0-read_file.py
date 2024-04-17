#!/usr/bin/python3
"""Defines a function to read text files."""


def read_file(filename=""):
    """Print the contents of a text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
