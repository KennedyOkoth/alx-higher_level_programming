#!/usr/bin/python3
"""a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide a matrix by a number div"""
    list_error = "matrix must be a matrix (list of lists) of integers/floats"
    len_error = "Each row of the matrix must have the same size"
    div_int_error = "div must be a number"
    div_zero_error = "division by zero"
    new_matrix = []
    new_list = []
    if not matrix:
        raise TypeError(list_error)
    if type(div) is not int and type(div) is not float:
        raise TypeError(div_int_error)
    if div == 0:
        raise ZeroDivisionError(div_zero_error)
    length = len(matrix[0])
    for x in matrix:
        if type(x) is not list:
            raise TypeError(list_error)
        if len(x) != length:
            raise TypeError(len_error)
        for item in x:
            if type(item) is not int and type(item) is not float:
                raise TypeError(list_error)
            num = item / div
            new_list.append(round(num, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
