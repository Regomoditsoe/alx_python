#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for col in matrix:
        for val_idx, val in col:
            print("{:d}".format(val), end="" if val_idx != len -1 else "")
        print()
