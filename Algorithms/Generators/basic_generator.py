def factors(n):
    """A basic way of generating factors"""
    results = []
    for k in range(1, n + 1):
        if n % k == 0:
            results.append(k)
    return results


def factors_generator(n):
    """Yield version of above"""
    for k in range(1, n + 1):
        if n % k == 0:
            yield k


print(factors(25))
