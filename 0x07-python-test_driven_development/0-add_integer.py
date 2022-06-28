#!/usr/bin/python3
"""This module defines the 'add_integer' function that returns the sum of a and b"""

def add_integer(a, b=98):
    '''Adds two integers or floats value together
    Args:
        a - int or float type
        b - int or float type, default value is 98
    Raises:
        TypeError if a and b is not an int or float type
    Return:
        The sum of a and b, an integer value only
    '''

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
