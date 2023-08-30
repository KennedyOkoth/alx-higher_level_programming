#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """A class Square that defines a square with a size private key"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size:"""

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """A method to retrieve/get/set the size of square

        Returns:
            size: size of square
        """
        return self.__size

    @property
    def position(self):
        """A property setter to set position

        Returns:
            position:
        """
        return self.__position

    @size.setter
    def size(self, value):
        """A method to set size

        Args:
             value (int, optional): size of the square

         Raises:
             TypeError: raised when the value is not of int type.
             ValueError: raised when value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """A method to set position

        Args:
            value (int):

        Raises:
            TypeError: _position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """A method to calculate area

        Returns:
            area: size sqaured
        """
        return self.__size**2

    def my_print(self):
        """A method to print a square of # character"""
        if self.__size == 0:
            print(" ")
            return
        [print(" ") for i in range(0, self.__position[1])]

        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()
