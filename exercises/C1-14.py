"""
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
dt3 = [1, 3, 5, 7, 9]


def distinct_pair_who_is_odd(data):
    for i in data:
        for j in data:
            if i == j:
                continue
            if i * j % 2 == 1:
                print(f"{i} * {j} produces an odd number which is", i * j)
                return True
    return False


print(distinct_pair_who_is_odd(dt1))
print(distinct_pair_who_is_odd(dt2))
print(distinct_pair_who_is_odd(dt3))
