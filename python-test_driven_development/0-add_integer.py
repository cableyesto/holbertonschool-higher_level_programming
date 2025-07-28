#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Documentation of the add integer module
The example module supplies one function, factorial().  For example,
>>> add_integer(2, 2)
4
"""


def add_integer(a, b=98):
    """Documentation of the add integer function
    >>> add_integer(2)
    100
    """

    if (isinstance(a, int) is False) and (isinstance(a, float) is False):
        raise TypeError("a must be an integer")
    if (isinstance(b, int) is False) and (isinstance(b, float) is False):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
