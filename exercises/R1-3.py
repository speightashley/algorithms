def minmax(data):
    """
    Write a short Python function, minmax(data), that takes a sequence of
    one or more numbers, and returns the smallest and largest numbers, in the
    form of a tuple of length two. Do not use the built-in functions min or
    max in implementing your solution.
    :param data: 
    :return: Tuple
    """

    low = None
    high = 0

    for num in data:
        if num > high:
            high = num
        if low is None:
            low = num
        elif num < low:
            low = num

    return low, high


numbers = [1, 5, 7, 9, 45, 87, 34, 76, 976, 34, 2, 65, 2]

print(minmax(numbers))
