#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for x in range(len(matrix)):
        new_matrix[x] = list(map(lambda x: x**2, matrix[x]))

    return new_matrix
