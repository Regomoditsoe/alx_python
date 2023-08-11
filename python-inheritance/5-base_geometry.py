#!/usr/bin/python3
"""Defines a BaseGeometry class"""

class BaseGeometry:
    """Represent the BaseGeometry"""
    def area(self):
        """Not implemented yet"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """An integer validating parameter
        Args:
            name: Parameter name.
            value: validating the parameter.
        Raises: 
            TypeError: must be an integer
            ValueError: must be <= 0."""
    if type(value) != int:
             raise TypeError("{} must be an integer".format(name))
    if value <= 0:
             raise ValueError("{} must be greater than 0".format(name))

