#!/usr/bin/python3
"""Rectangle module."""


class Rectangle:
    """Rectangle class."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

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
        
        symbol = str(self.print_symbol)
        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append(symbol * self.__width)
        return "\n".join(rectangle_str)

    def __repr__(self):
        """Return repr."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Delete message."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
