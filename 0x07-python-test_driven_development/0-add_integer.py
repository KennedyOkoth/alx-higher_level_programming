#!/usr/bin/python3
"""Addition function"""


def add_integer(a, b=98):
    """Adds two intergers

    Args:
        a (int): number
        b (int, optional): number. Defaults to 98.

    Raises:
        TypeError: raised when a or b is not int

    Returns:
        int: sum of two numbers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
