#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON-formatted string.
    Parameters:
    my_obj (Any): The Python object to be converted to a JSON string
    Returns:str: A JSON-formatted string representation of the input
    """
    json_str = json.dumps(my_obj)
    return json_str
