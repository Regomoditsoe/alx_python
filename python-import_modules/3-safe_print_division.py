#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = (a / b)
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result

a = 0
b = 2

result = safe_print_division(a, b)
if result is not None:
    print("{} / {} = {}".format(a, b, result))

