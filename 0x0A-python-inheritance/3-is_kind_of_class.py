#!/usr/bin/python3
"""
module: 2-is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Function: is_kind_of_class
    Checks if an object is an instance of a specific class or a subclass.

    Args:
    - obj (object): The object to be checked.
    - a_class (class): The class to compare the object against.

    Returns:
    - bool: True if the object is an instance of the specified class or a
    subclass, False otherwise.
    """
    return isinstance(obj, a_class)
