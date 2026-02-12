#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Student class with first_name, last_name, and age attributes"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance

        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance

        Args:
            attrs: list of attribute names to retrieve (optional)

        Returns:
            Dictionary representation of the student
        """
        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list) and \
                all(isinstance(attr, str) for attr in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
