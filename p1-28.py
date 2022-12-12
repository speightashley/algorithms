"""
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
"""


def divide_until_two(number):
    count = 0
    while number >= 2:
        number = number // 2
        count = count + 1
    return count


print(divide_until_two(2))
