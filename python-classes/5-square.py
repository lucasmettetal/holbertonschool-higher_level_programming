#!/usr/bin/python3
"""This module defines a Square class with printing capability."""


class Square:
    """A class that defines a square with printing capability.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square. Defaults to 0.
        """
        self.size = size   # Passe par le setter → validation automatique

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

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
        self.__size = value

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the '#' character.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
