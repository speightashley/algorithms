def is_multiple(n, m):
    """
    Write a short Python function, is multiple(n, m), that takes two integer
    values and returns True if n is a multiple of m, that is, n = mi for some
    integer i, and False otherwise.
    :param n:
    :param m:
    :return: Boolean
    """
    if n % m == 0:
        return True
    else:
        return False


print(is_multiple(12, 5))
