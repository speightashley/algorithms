"""Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function.
"""

n = 20

x = sum([n * n for n in range(n) if n % 2 == 0])

print(x)

