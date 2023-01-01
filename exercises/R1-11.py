"""Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256]."""

double_up = [2 ** n for n in range(0, 9)]

print(double_up)
