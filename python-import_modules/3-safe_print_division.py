#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = (a / b)
    except ZeroDivisionError:
        result = None
    finally:
        if not hasattr(safe_print_division, "printed"):
            safe_print_division.printed = set()

        if result is not None and (a, b) not in safe_print_division.printed:
            safe_print_division.printed.add((a, b))
            print("Inside result: {}".format(result))
            print("{} / {} = {}".format(a, b, result))
        return result
