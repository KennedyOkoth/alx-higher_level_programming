#!/usr/bin/python3
"""A function to append text and the end."""


def append_write(filename="", text=""):
    """Returns the number of characters added:"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
