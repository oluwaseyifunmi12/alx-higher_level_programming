#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    my_matrix = []
    for row in matrix:
        result = list(map(lambda x: x ** 2, row))
        my_matrix.append(result)
    return my_matrix
