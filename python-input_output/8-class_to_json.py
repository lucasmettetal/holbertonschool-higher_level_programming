#!/usr/bin/python3
"""Module that returns the dictionary description for JSON serialization"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj: instance of a Class

    Returns:
        Dictionary description of the object
    """
    return obj.__dict__
