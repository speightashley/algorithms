"""Give a single command that computes the sum from Exercise R-1.4,
relying on Python’s comprehension syntax and the built-in sum function."""

x = int(input("Give me a number "))


print(sum([k**2 for k in range(x + 1)]))
