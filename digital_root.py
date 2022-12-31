def digital_root(n):
    """
    Takes an integer and adds up all of the digits until it gets down to a single digit
    :param n:
    :return:
    """
    # ...
    if n < 10:
        return n
    else:
        n = n % 10 + digital_root(n // 10)
        return digital_root(n)


print(digital_root(24567864))
