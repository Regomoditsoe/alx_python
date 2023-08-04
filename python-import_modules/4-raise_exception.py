#!/usr/bin/python3

def raise_exception():
    a = "Raise exception"
    b = 98
    try:
        result = a + b
    except TypeError as E:
        print("Exception raised")
