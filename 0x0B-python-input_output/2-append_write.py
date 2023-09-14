#!/usr/bin/python3
"""A function to append text and the end."""


def append_write(filename="", text=""):
    with open(filename, "a+", encoding="utf-8") as file:
        current_position = file.tell()
        file.write(text)
        file.seek(0, 2)
        new_position = file.tell()
        num_characters_added = new_position - current_position
        return num_characters_added
