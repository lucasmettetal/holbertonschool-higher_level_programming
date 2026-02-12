#!/usr/bin/python3
"""Module that appends a string to a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns
    the number of characters added

    Args:
        filename: name of the file to append to (default: "")
        text: text to append to the file (default: "")

    Returns:
        The number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
