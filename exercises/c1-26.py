"""
Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”
"""
import operator


def arrithmatic_checker(a, b, c):
    basic_operators = [operator.add, operator.sub, operator.mul, operator.floordiv]  # Methods for operators
    results = []
    for op in basic_operators:  # Cycle through the operator methods on the numbers
        if a == op(b, c):
            results.append(op.__name__)
        if c == op(b, a):
            results.append(op.__name__)

    return results



def another_function(a, b, c):
    return a + b + c


print(arrithmatic_checker(1, 2, 3))
print(arrithmatic_checker(2, 2, 4))
print(arrithmatic_checker(5, 10, 2))
