"""Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally."""

my_list = [chr(value) for value in range(97, 123)]
# chr() returns the ascii letter by number / ord() returns the number by letter

print(my_list)

my_list2 = [ord('a')]

print(my_list2)
