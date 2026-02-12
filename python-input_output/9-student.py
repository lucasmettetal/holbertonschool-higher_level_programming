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

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance

        Returns:
            Dictionary representation of the student
        """
        return self.__dict__
