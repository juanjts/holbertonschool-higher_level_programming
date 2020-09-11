#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [list(map((lambda x: x * x), b)) for b in matrix]
    return new
