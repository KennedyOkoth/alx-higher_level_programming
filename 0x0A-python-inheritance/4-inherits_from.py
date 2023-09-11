#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Function: inherits_from

    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from a specific class.

    Args:
    - obj (object): The object to be checked.
    - a_class (class): The class to compare the object against.

    Returns:
    - bool: True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class, False otherwise.
    """
    return type(obj) != a_class and isinstance(obj, a_class)
