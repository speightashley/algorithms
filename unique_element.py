def find_uniq(arr):
    options = list(set(arr))

    for option in options:
        frequency = 0
        for item in arr:
            if item == option:
                frequency += 1
        if frequency == 1:
            return option



print(find_uniq([1, 1, 3, 1, 1, 1, 1]))
