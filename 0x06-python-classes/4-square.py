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
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """A method to calculate area

        Returns:
            area: size sqaured
        """
        return self.__size**2

    def get_size(self):
        return self.__size
