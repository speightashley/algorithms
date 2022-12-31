"""
Factorial with recursion

"""


def factorial(number: int):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(10))


def fibonacci(start):
    if start == 0:
        return 0
    else:
        return 
