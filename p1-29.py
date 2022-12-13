"""
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
"""
import itertools


def all_combos(string):
    """
    Write a Python program that outputs all possible strings formed by using
    the characters c , a , t , d , o , and g exactly once.
    :param string: 
    :return: tuple
    """
    perm = itertools.permutations(string, len(string))
    for i in perm:
        print(i)


my_string = "catdog"


all_combos(my_string)
