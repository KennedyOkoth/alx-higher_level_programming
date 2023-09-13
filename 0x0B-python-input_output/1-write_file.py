#!/usr/bin/python3
"""A function to write in a file"""


def write_file(filename=''):
    """My writing in a file function"""
    with open(filename, "w", encoding="utf-8") as f:
        print(f.write('This is a text\n'))
