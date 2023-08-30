#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """A class Square that defines a square with a size private key"""

    def __init__(self, size=0):
        """Instation with size

        Args:
            size (Any type): Size of the square
        """
        self.__size = size
