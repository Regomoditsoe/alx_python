#!/usr/bin/python3
"""Define the class BaseGeometry"""

class BaseGeometry:
    """ Represents the BaseGeometry"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")
    def __dir__(self):
        return ['area']
