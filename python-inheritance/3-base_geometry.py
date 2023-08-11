#!/usr/bin/pythoni3
"""Define an empty class"""

class BaseGeometry:
    """"A class that represents a Base Geometry"""
    def __dir__(self):
        return list(super().__dir__()) + ["__class__"]
