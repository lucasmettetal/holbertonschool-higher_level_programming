#!/usr/bin/python3
"""Rectangle module."""


class Rectangle:
    """Rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width."""
        return self.__width

    @height.setter
    def height(self, value):
        """Set height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append("#" * self.__width)
        return "\n".join(rectangle_str)

    def __repr__(self):
        """Return repr."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Delete message."""
        print("Bye rectangle...")
