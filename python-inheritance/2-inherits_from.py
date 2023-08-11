#!/usr/bin/python3
"""Define an inheretance"""
def inherits_from(obj, a_class):
    """Check if the object is an instance of a class inherited
    Args:
        obj: object to be checked.
        a_class: the class to match the object to.
    Return: True - if the object is an instance of class.
        False - Otherwise."""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        True
