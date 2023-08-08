#!/usr/bin/python3
"""Define class square"""

class Square:
    """Represents the square"""

    def __init__(self,size=0):
        """Initialize new square
        Args:
            size(int): The size of a new square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
