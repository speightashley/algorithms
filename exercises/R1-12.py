import random


def choice_ash(data):
    """Python’s random module includes a function choice(data) that returns a
    random element from a non-empty sequence. The random module in-
    cludes a more basic function randrange, with parameterization similar to
    the built-in range function, that return a random choice from the given
    range. Using only the randrange function, implement your own version
    of the choice function."""
    length = len(data)
    random_element = random.randrange(0, length)
    return data[random_element]


random_data = [1, 5, 7, 45, 37, 23, 76]

print(choice_ash(random_data))

