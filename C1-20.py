"""
Python’s random module includes a function shuﬄe(data) that accepts a
list of elements and randomly reorders the elements so that each possi-
ble order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuﬄe function.

"""

import random

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list2 = [5, 4, 7, 3, 8, 9, 3, 2, 7, 9, 0]


def my_shuffle(data):
    """
    Shuffles a list into a random order
    :param data: List
    :return: List
    """
    new_list = []
    while len(data) > 0:
        new_element = data.pop(random.randint(0, len(data) - 1))
        new_list.append(new_element)

    return new_list


print(my_shuffle(my_list2))
