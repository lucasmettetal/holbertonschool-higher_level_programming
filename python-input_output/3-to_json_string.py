#!/usr/bin/python3
"""Module that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)

    Args:
        my_obj: object to convert to JSON string

    Returns:
        JSON string representation of the object
    """
    return json.dumps(my_obj)
