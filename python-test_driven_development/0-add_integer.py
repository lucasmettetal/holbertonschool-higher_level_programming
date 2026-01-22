#!/usr/bin/python3
def add_integer(a, b=98):
    """Return the addition of two integers.

    Args:
        a (int/float): The first integer.
        b (int/float): The second integer (default is 98).

    Raises:
        TypeError: If either a or b is not an integer or float.

    Returns:
        int: The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
