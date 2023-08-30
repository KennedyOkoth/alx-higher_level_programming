#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """A class Square that defines a square with a size private key"""

    def __init__(self, size=0):
        """Instantiation with optional size:

        Args:
            size (int, optional): size of the square

        Raises:
            TypeError: raised when the value is not of int type.
            ValueError: raised when value is less than 0
        """

        self.__size = size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def size(self):
        """A method to retrieve/get/set the size of square

        Returns:
            size: size of square
        """
        return self.__size

    def area(self):
        """A method to calculate area

        Returns:
            area: size sqaured
        """
        return self.__size**2
