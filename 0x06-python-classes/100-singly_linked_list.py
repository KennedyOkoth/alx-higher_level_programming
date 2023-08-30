#!/usr/bin/python3


class Node:
    """defins a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """For retrieving data

        Args:
            data (int): A number
            next_node (node, optional): A node. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """a property

        Returns:
            _int: a number
        """
        return self.__data

    @data.setter
    def data(self, value):
        """a property setter

        Args:
            value (int): data

        Raises:
            TypeError: Raised when type is not integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a node object")
        self.__next_node = value


class SinglyLinkedList:
    """_summary_"""

    def __init__(self):
        """_summary_"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        current = self.__head
        result = []
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
