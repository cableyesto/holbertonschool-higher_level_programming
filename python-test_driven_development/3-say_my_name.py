#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Documentation of the say my name module"""


def say_my_name(first_name, last_name=""):
    """Documentation of the say my name function"""

    if (isinstance(first_name, str) is False):
        raise TypeError("first_name must be a string")
    if (isinstance(last_name, str) is False):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
    return
