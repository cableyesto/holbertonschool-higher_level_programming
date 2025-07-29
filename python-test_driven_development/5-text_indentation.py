#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Documentation of the text intendentation module"""


def text_indentation(text):
    """Documentation of the text indentation function"""

    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    buffer = []
    for char_idx, char in enumerate(text):
        if char == "." or char == "?" or char == ":":
            buffer.append(char)
            print("".join(buffer), end="")
            print("\n")
            buffer = []
        elif char == " ":
            if text[char_idx - 1] == "." or text[char_idx - 1] == "?" or \
               text[char_idx - 1] == ":":
                continue
            else:
                buffer.append(char)
        else:
            buffer.append(char)

    print("".join(buffer), end="")

    return
