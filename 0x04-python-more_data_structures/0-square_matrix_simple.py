#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    matrix_s = [[x*x for x in row] for row in matrix]
    return matrix_s
