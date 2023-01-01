"""
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1.
"""

my_array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_array2 = [7, 5, 3, 4, 6, 8, 9, 6, 4]


def product_of_two(list1, list2):
    """
    Write a short Python program that takes two arrays a and b of length n
    storing int values, and returns the dot product of a and b. That is, it returns
    an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1.
    :param list1: list of equal length to param 2
    :param list2: list of equal length to param 1
    :return: list of the product of each element of list1 and list2
    """
    new_list = []
    for num in range(len(list1)):
        new_list.append(list1[num] * list2[num])
    return new_list


print(product_of_two(my_array1, my_array2))
