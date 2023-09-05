#!/usr/bin/python3
"""
This is the "Rectangle"  module.

This module provides a Rectangle class.
"""


class Rectangle:
    """A Rectangle class with attributes  width and height"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object with the given width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:

            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def __str__(self):
        """Return a string representation of the rectangle using '#'
        characters.
        """
        count = ""
        if self.__height == 0 or self.__width == 0:
            return count
        for x in range(self.__height):
            count += "#" * self.__height
            if x is not self.__height - 1:
                count += "\n"
        return count

    def area(self):
        """
        Calculate and return the area of the rectangle.
        Returns:
        float: The area of the rectangle, which is the product of its height
        and width.
        """
        reactangle_area = self.__height * self.__width
        return reactangle_area

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle, which is 2 times the sum of
            its height and width,
            unless either the height or width is 0, in which case the
            perimeter is 0.
        """
        if self.__height == 0 or self.__width == 0:
            rectangle_perimeter = 0
        else:
            rectangle_perimeter = 2 * (self.__height + self.__width)
        return rectangle_perimeter

    def __repr__(self):
        """Return a string representation of the rectangle for debugging."""
        return f"Rectangle({self.__width}, {self.__height})"
