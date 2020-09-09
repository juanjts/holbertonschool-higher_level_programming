#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for f in range(len(matrix)):
        for c in range(len(matrix[f])):
            print('{:d}'.format(matrix[f][c]), end='')
            if c != len(matrix[f])-1:
                print(end=' ')
        print()
