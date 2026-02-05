#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize a Rectangle with validated private width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
