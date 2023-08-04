#!/usr/bin/python3
import sys

def print_arguments(*argv):
    num_args = len(argv)

    if num_args == 0:
        print("0 arguments.")
        return

    if num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
        args = sys.argv[1:]
        print_arguments(*args)
