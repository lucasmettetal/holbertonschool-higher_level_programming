#!/usr/bin/python3
"""Module that writes an Object to a text file using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: object to save
        filename: name of the file to save to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
