#!/usr/bin/python3
"""This module defines a Square class with property accessors."""


class Square:
    """A class that defines a square with property-based size management.

    Attributes:
        _size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self._size * self._size
