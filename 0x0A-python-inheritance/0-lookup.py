#!/usr/bin/python3
class Item:
    """
    A class representing items with a name and age.

    Attributes:
    - name (str): The name of the item.
    - age (int): The age of the item.

    Class Attributes:
    - all (list): A list to store all created Item instances.
    """

    all = []

    def __init__(self, name, age):
        """
        Initializes a new Item instance with the given name and age.

        Args:
        - name (str): The name of the item.
        - age (int): The age of the item.
        """
        self.age = age
        self.name = name
        Item.all.append(self)


item1 = Item("Item1", 5)
item2 = Item("Item2", 8)

# Accessing all created Item instances
all_items = Item.all
