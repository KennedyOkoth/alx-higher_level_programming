#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class for representing and manipulating rectangles.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): The unique identifier for the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Initializes a Rectangle instance with specified width, height,
            position, and optional ID.
        width (property):
            Getter method for retrieving the width of the rectangle.
        width (setter):
            Setter method for setting the width of the rectangle.
        height (property):
            Getter method for retrieving the height of the rectangle.
        height (setter):
            Setter method for setting the height of the rectangle.
        x (property):
            Getter method for retrieving the x-coordinate of the rectangle's
            position.
        x (setter):
            Setter method for setting the x-coordinate of the rectangle's
            position.
        y (property):
            Getter method for retrieving the y-coordinate of the rectangle's
            position.
        y (setter):
            Setter method for setting the y-coordinate of the rectangle's
            position.
        area(self):
            Calculates and returns the area of the rectangle.
        display(self):
            Displays the rectangle on the console with '#' characters.
        update(self, *args, **kwargs):
            Updates the attributes of the rectangle using positional or
            keyword arguments.
        to_dictionary(self):
            Converts the rectangle's attributes into a dictionary.
        __str__(self):
            Returns a string representation of the rectangle in the format:
            "[Rectangle] (ID) X/Y - Width/Height".
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance with specified width, height,
        position, and optional ID.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner of the
            rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner of the
            rectangle. Defaults to 0.
            id (int, optional): The unique identifier for the rectangle.
            Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.height * self.width

    def display(self):
        """
        Displays the rectangle on the console with '#' characters.
        The rectangle is positioned based on its x and y attributes.
        """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle using positional or keyword
        arguments.

        Args:
            *args: Positional arguments in the order (ID, width, height, x, y).
            **kwargs: Keyword arguments for updating specific attributes (id,
            width, height, x, y).
        """
        if args and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Converts the rectangle's attributes into a dictionary.

        Returns:
            dict: A dictionary containing the rectangle's attributes.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

    def __str__(self):
        """
        Returns a string representation of the rectangle in the format:
        "[Rectangle] (ID) X/Y - Width/Height".

        Returns:
            str: A string representation of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )
