#!/usr/bin/python3
"""Contains a python string"""

import json


def from_json_string(my_str):
    """
    Converts a json steing to python object.
    Arguments:
    my_str: a json string

    Returns a python object
    """
    data = json.loads(my_str)
    return data
