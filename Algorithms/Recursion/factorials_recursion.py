def factorials(n):
    if n == 0:
        return 1
    else:
        return n * factorials(n - 1)
