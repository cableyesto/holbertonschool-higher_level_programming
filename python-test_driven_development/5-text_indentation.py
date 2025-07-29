#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Documentation of the text intendentation module"""


def text_indentation(text):
    """Documentation of the text indentation function"""

    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    buffer = []
    number_of_separators = 0
    for char in text:
        if char == "." or char == "?" or char == ":":
            number_of_separators += 1
            buffer.append(char)
            print("".join(buffer), end="")
            print("\n")
            buffer = []
        else:
            buffer.append(char)

    print("".join(buffer), end="")

    return
