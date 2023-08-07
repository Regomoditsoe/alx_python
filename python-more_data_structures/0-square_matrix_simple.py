#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_n = [row[:] for row in matrix]

    for init in range(len(matrix)):
        matrix_n[init] = list(map(lambda x: x**2, matrix[init]))

    return (matrix_n)
