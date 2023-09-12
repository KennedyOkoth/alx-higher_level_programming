#!/usr/bin/python3
""" Defines a base geometry class BaseGeometry.
"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int):
        """Validate that a value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greator than 0".format(name))


class Rectangle(BaseGeometry):
    """Represents a rectangle."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
