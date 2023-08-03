#!/usr/bin/python3

def validate_password(password):
    if len(password) < 8:
        return False

    contains_digit = False
    contains_lowercase = False
    contains_uppercase = False

    for char in password:
        if char.idigit():
            contains_digit = True
        elif char.islower():
           contains_lowercase = True
        elif char.isupper():
            contains_uppercase = True

    if not (contains_digit and contains_lowercase and contains_uppercase):
        return False

    if ' ' in password:
        return False

    return True

