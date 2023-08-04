#!/usr/bin/python3

def raise_exception_msg(message=""):
    if not message:
        message = ""
    raise NameError(message)

try:
    raise_exception_msg("")
except NameError as ne:
    print("", ne)

