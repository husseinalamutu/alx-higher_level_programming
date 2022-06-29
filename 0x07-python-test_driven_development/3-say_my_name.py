#!/usr/bin/python3
"""This module defines 'say_my_name' function that prints 'My name is <first name> <last name>"""

def say_my_name(first_name, last_name=""):
    '''
    Args:
        first_name - First name
        last_name - Surname
    Raises:
        TypeError 'first name must be a string' or 'last name must be a string'
    Returns:
        My name is <first_name> <last_name>
    '''
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    return "My name is {} {}".format(first_name, last_name)