#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

The_Last_digit = abs(number) % 10
print('The last string digit of', number, 'is', The_Last_digit, end=" ")

if The_Last_digit > 5:
    print('and is greater than 5');
elif The_Last_digit == 0:
    print('and is 0');
else:
    print('and is less than 6 and not 0');
