#!/usr/bin/python3
def uppercase(str):
    ascii_difference = 32
    letter_a_ascii = 97
    letter_z_ascii = 122
    letter_A_ascii = 65
    letter_Z_ascii = 90
    space_ascii = 32
    str_out = []
    for char in str:
        if ord(char) < (letter_z_ascii + 1) and ord(char) >= letter_a_ascii:
            char_upper_num = ord(char) - ascii_difference
            str_out.append(chr(char_upper_num))
        elif ord(char) < (letter_Z_ascii + 1) and ord(char) >= letter_A_ascii:
            str_out.append(char)
        elif char.isnumeric():
            str_out.append(char)
        elif ord(char) == space_ascii:
            str_out.append(char)
        else:
            continue
    print("{}".format("".join(str_out)))
