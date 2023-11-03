#!/usr/bin/python3
"""Defines a class of a function"""
def is_kind_of_class(obj, a_class):
    """Check if  the object is an instance or of a class
    Args:
        obj: object to be dependant on
        a_class: the class needed to match the object
    Returns: True  if the object is of an instance.
        False:  Otherwise."""
    return isinstance(obj, a_class)
