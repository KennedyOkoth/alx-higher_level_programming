#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle class.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
                Defaults to 0.
            y (int, optional): The y-coordinate of the square's position.
                Defaults to 0.
            id (int, optional): The ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        int: The size of the square. Can be accessed and updated through this
        property.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size property. Sets both width and height to the
        same value.

        Args:
            value (int): The new size for the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square instance.

        Args:
            *args: Variable-length argument list. If provided, it should
            contain the
                following (in order): ID, size, x, y.
            **kwargs: Keyword arguments for updating the attributes. Valid keys
                include "id", "size", "x", and "y".
        """
        if args and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Convert the Square instance to a dictionary representation.

        Returns:
            dict: A dictionary containing the square's attributes.
                Keys: "id", "size", "x", "y".
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y,
        }

    def __str__(self):
        """
        String representation of the Square instance.

        Returns:
            str: A string in the format "[Square] (ID) X/Y - Size".
        """
        return "[Square] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )
