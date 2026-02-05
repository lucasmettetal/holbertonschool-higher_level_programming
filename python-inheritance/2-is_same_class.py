#!/usr/bin/python3
"""
This module defines a function that checks if an object is an
instance of a class.
"""


def is_same_class(obj, a_class):
    """
    Return True if the object is an instance of the specified class,
    otherwise False.
    """
    return type(obj) is a_class
