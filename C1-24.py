"""
Write a short Python function that counts the number of vowels in a given
character string.
"""


def number_of_vowels(string):
    """
    Write a short Python function that counts the number of vowels in a given
    character string.
    :param string: string
    :return: int
    """
    count = 0
    for char in string.lower():
        if char in "aeiou":
            count += 1
    return count


print(number_of_vowels("This is a sentence with a few vowels in AEIUO it"))
