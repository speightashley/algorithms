"""Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct)."""


def unique_numbers(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False


data_list1 = [1, 2, 2, 4, 5, 6, 7, 8]
data_list2 = [1, 2, 3, 4, 5, 6, 7, 8]

print(unique_numbers(data_list1))
print(unique_numbers(data_list2))
