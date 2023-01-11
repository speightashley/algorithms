def iteration_sort(list):
    for x in range(1, len(list)):  # from 1 to n - 1
        cur = list[x]  # Current element to be inserted
        j = x  # Find correct index j for Current
        while list[j - 1] > cur and j > 0:  # Element list[j - 1]
            list[j] = list[j - 1]
            j -= 1
            list[j] = cur  # current is now in the right place
    return list


my_sequence = [2, 1, 5, 7, 4, 3, 8]
print(iteration_sort(my_sequence))
