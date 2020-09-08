#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for f in range(len(matrix)):
        for c in range(len(matrix[f])):
            print("{}".format(matrix[f][c]), end=" ")
        print()
