#!/usr/bin/python3

def raise_exception_msg(message=""):
    if not message:
        message = ""
    raise NameError(message)

try:
    raise_exception_msg("Python is cool")
except NameError as ne:
    print("C is fun", ne)

