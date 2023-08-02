#!/usr/bin/python3

def pow(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result
result_1 = pow(2, 2)
print(result_1)

result_2 = pow(98, 2)
print(result_2)

result_3 = pow(98,0)
print(result_3)

result_4 = pow(100, -2)
print(result_4)

result_5 = pow(-4, 5)
print(result_5)
