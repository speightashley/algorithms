"""
[expression for value in iterable if condition]

"""

squares = []
n = 20

for k in range(1, n + 1):
    squares.append(k * k)

# List comprehension method

squares = [k * k for k in range(1, n + 1)]

factors = [k for k in range(1, n + 1) if n % k == 0]
