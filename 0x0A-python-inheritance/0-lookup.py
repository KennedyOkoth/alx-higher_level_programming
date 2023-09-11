#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    - obj (object): The object for which to retrieve attributes and methods.

    Returns:
    - list: A list containing the names of attributes and methods.
    """
    return dir(obj)


# Example usage:
class Example:
    def __init__(self):
        self.name = "Example"

    def greet(self):
        return f"Hello, I'm {self.name}!"


example_obj = Example()
result = lookup(example_obj)
print(result)
