#!/usr/bin/python3
"""Defines a class that checks a function"""

def is_same_class(obj, a_class):
    """Checks if the object if an instance of a specified class
    Args:
        obj: The object to be checked
        a_class: the class we need to match with the object
        return: True - object is of an instance.
        False - otherwise."""
    if type(obj) == a_class:
        return True
    else:
        return False
