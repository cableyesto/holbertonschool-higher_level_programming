#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Documentation of the square module"""


class Square:
    """Square class with size private attribute"""
    def __init__(self, size=0):
        """Initialize the class"""
        self.__size = size

    @property
    def size(self):
        """Getter of the size private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of the size private attribute"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public method to calculate the area of square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square on the command line"""
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("{}".format("#"), end="")
                print("")
        else:
            print("")
