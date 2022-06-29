#!/usr/bin/python3
"""This module defines 'print_square' function"""

def print_square(size):
    if type(size) == float  and size < 0:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()