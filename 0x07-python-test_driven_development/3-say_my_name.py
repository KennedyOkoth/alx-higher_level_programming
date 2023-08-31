#!/usr/bin/python3
""" A name printing function"""


def say_my_name(first_name, last_name=""):
    """A function that prints a name

    Args:
        first_name (str): name
        last_name (str, optional): name. Defaults to "".

    Raises:
        TypeError: raised when first name or last name is not a dtring
        TypeError: _description_

    Returns:
        string: string
    """
    if type(first_name) is not str or type(last_name) is not str:
        raise TypeError("first_name must be a string or last_name must be a string")
    print(f"My name is {first_name} {last_name}")
