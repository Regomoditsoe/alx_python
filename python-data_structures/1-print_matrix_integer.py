#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_idx, val in enumerate(row):
            print("{:d}".format(col), end="" if col_idx != len(row) -1 else "")
        print()
