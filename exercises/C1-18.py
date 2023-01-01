"""Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
increments increase in 2, 4, 6, 8, 10, 12 etc"""

my_list = [n * (n + 1) for n in range(10)]

print(my_list)

