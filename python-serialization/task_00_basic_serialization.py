#!/usr/bin/python3
"""
Basic serialization module that adds the functionality to serialize
a Python dictionary to a JSON file and deserialize the JSON file to
recreate the Python Dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize and save data to the specified file.

    Args:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file.
                  If the output file already exists it should be replaced.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize data from the specified file.

    Args:
        filename: The filename of the input JSON file

    Returns:
        A Python Dictionary with the deserialized JSON data from the file.
    """
    with open(filename, 'r') as f:
        return json.load(f)
