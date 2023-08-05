#!/usr/bin/python3

def no_c(my_string):
    """Remove 'c' and 'C' fromstring"""
    copy = [i for i in my_string if i != 'c' and i != 'C']
    new_string = "".join(copy)
    return new_string
