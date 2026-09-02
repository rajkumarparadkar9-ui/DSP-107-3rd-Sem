
# Program 1: Built-in Module (math)

import math

num = 16

print("Square root:", math.sqrt(num))
print("Factorial:", math.factorial(5))
print("Power:", math.pow(2, 3))
print("Log:", math.log(10))


# Program 2: Functional Programming Module

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print("Sum using reduce:", result)


# Program 3: User-defined Module Concept

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


print("Addition:", add(10, 5))
print("Multiplication:", multiply(10, 5))