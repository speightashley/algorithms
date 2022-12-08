"""Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing."""

"""
1. check length of input list
2. create an empty list
3. loop over first list and append each list item at the last position to the new list
4. Return the new list
"""

my_list = [n for n in range(50)]

print(my_list)


def reverse_a_list(data):
    empty_list = []
    length = len(data)
    while length > 0:
        empty_list.append(data[length - 1])
        length -= 1

    return empty_list


print(reverse_a_list(my_list))
