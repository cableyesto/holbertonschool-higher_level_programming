#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Documentation of the say my name module"""


def print_square(size):
    """Documentation of the say my name function"""

    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")

    if size != 0:
        for i in range(size):
            for j in range(size):
                print("{}".format("#"), end="")
            print("")

    return
