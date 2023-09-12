#!/usr/bin/python3
""" function that returns the list
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    - obj (object): The object for which to retrieve attributes and methods.

    Returns:
    - list: A list containing the names of attributes and methods.
    """
    return dir(obj)
