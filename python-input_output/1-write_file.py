#!/usr/bin/python3
"""Module that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number
    of characters written
    Args:
        filename: name of the file to write to (default: "")
        text: text to write to the file (default: "")
    Returns:
        The number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
