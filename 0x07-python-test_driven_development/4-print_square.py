#!/usr/bin/python3
"""a function that prints a square with the character #"""


def print_square(size):
    """a function that prints a square with the character #

    Args:
        size (int):

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        TypeError: size must be an integer
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for c in range(size):
        print("#" * size, end="")
        print()
