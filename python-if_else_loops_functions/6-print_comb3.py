#!/usr/bin/python3
i = 0
while i < 9:
    j = i + 1
    while j < 10:
        # print("{}{}".format(i, j), end=', ')
        if i == 8 and j == 9:
            print("89")
            break
        else:
            print("{}{}".format(i, j), end=', ')
        j += 1
    if j == 9:
        break
    i += 1
