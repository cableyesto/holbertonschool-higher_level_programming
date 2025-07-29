#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Documentation of the matrix divided"""


def matrix_divided(matrix, div):
    """Documentation of the matrix divided function"""

    if (isinstance(div, int) is False) and (isinstance(div, float) is False):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    len_matrix_rows = []

    for row_idx in range(len(matrix)):
        len_matrix_rows.append(len(matrix[row_idx]))
        for col_idx in range(len(matrix[row_idx])):
            if (isinstance(matrix[row_idx][col_idx], int) is False) and \
               (isinstance(matrix[row_idx][col_idx], float) is False):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    if len_matrix_rows.count(len_matrix_rows[0]) != len(len_matrix_rows):
        raise TypeError("Each row of the matrix must have the same size")

    matrix_result = []

    for row_index, row in enumerate(matrix):
        list_inter = []
        for col_index in range(len(matrix[row_index])):
            list_inter.append(round(matrix[row_index][col_index] / div, 2))
        matrix_result.append(list_inter)

    return matrix_result
