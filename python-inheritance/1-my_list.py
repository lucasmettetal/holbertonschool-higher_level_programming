#!/usr/bin/python3
"""Defines a MyList class that inherits from list."""


class MyList(list):
    """Custom list class with a sorted print method."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
