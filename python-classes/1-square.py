#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute size.
"""


class Square:
    """A class that defines a square.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
