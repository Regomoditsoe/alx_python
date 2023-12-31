#!/usr/bin/python3

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return[0]

    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n:
        next_sequence = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_sequence)

    return fibonacci_numbers
