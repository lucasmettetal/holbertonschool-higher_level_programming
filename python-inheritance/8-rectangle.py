#!/usr/bin/python3
"""Module that defines a Rectangle class.

This module provides a Rectangle class that inherits from BaseGeometry
and validates width and height as positive integers.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class that inherits from BaseGeometry.

    This class represents a rectangle with validated width and height
    dimensions.

    Attributes:
        __width: The width of the rectangle (private).
        __height: The height of the rectangle (private).
    """

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width: The width of the rectangle (must be a positive integer).
            height: The height of the rectangle (must be a positive integer).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
