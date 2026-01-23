#!/usr/bin/python3
"""
Module 5-text_indentation
Contains a function that prints text with 2 new lines after '.', '?', ':'.
"""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    start_of_line = True
    while i < len(text):
        if text[i] == ' ' and start_of_line:
            i += 1
            continue
        start_of_line = False
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print("\n")
            i += 1
            start_of_line = True
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
