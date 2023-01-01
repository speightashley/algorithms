def insertion_sort(a: list) -> list:
    """
    Sort a list of comparable elements into non decreasing order
    :param a: List
    :return: List
    """
    for k in range(1, len(a)):
        cur = a[k]
        j = k

        while j > 0 and a[j - 1] > cur:
            a[j] = a[j - 1]
            j -= 1
        a[j] = cur
    return a


my_list = [5, 7, 3, 9, 5, 3, 7, 2, 9]

my_sorted_list = insertion_sort(my_list)

print(my_sorted_list)
print(my_list)

