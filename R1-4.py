def sum_of_squares(n):
    """
    Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the positive integers smaller than n
    :param n: 
    :return: int
    """
    total = 0
    while n > 0:
        total = total + n * n
        n = n - 1
    return total


print(sum_of_squares(7))
