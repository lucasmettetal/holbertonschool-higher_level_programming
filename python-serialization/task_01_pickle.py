#!/usr/bin/python3
"""
Pickling Custom Classes module.
Learn how to serialize and deserialize custom Python objects using pickle.
"""
import pickle


class CustomObject:
    """
    A custom Python class with name, age, and is_student attributes.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the person
            age (int): The age of the person
            is_student (bool): Whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a specific format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of the object and save it to a file.

        Args:
            filenam (str): The filename where the object will be saved
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize and load an instance of CustomObject from a file.

        Args:
            filename (str): The filename to load the object from

        Returns:
            CustomObject: The deserialized instance, or None if an error occurs
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.PickleError, EOFError, Exception):
            return None
