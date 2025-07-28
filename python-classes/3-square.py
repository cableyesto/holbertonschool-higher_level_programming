#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Documentation of the square module"""


class Square:
    """Square class with size private attribute"""
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public method to calculate the area of square"""
        return self.__size ** 2
