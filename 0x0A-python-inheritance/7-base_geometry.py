#!/usr/bin/python3
""" Defines a base geometry class BaseGeometry.
"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int):
        assert type(name) == str
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greator than 0")
        self.value = value
