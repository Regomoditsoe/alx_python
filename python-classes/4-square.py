#!/usr/bin/python3
"""Define a class square"""
class Square:
    """"Represents a square"""
    def __init__(self, size):
        """A new square to initialize
        Args:
            size(int): The size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Get or set the current square size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size is >=0")
        else:
            self.__size = value

    def area(self):
        """Return current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Print square with # character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
