def sum_of_odd_squares(n):
    """
    Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the odd positive integers smaller than n.
    :param n: 
    :return: int
    """
    total = 0

    while n > 0:
        if n % 2 == 1:
            n -= 1
        if n % 2 == 0:
            total += (n * n)
            n -= 1

    return total


print(sum_of_odd_squares(4))
