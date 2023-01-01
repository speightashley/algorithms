"""
A common punishment for school children is to write out a sentence mul-
tiple times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.
"""


def multiply_sentence_with_typos(a_string, number_of_lines):
    """
    Returns the string duplicated 100 times on separate lines with line numbers and random typos
    :param number_of_lines: int
    :param a_string: the string to write down
    :return:
    """
    import random
    average_mistake_number = number_of_lines // 8
    for i in range(number_of_lines):
        if i > 0 and i % average_mistake_number == 0:  # Not really random but inserts 8 mistakes in there
            word_list = a_string.split()  # Split the sentence into a list of words
            random_word = word_list[random.randint(0, len(word_list) - 1)]  # Select a random word to change
            random_letter = random_word[random.randint(0, len(random_word) - 1)]  # Select a random letter from that
            # word
            word_index = word_list.index(random_word)  # Get the index of the random word
            word_list[word_index] = random_word.replace(random_letter, chr(random.randint(97, 120)))  # Replace the
            # selected letter with a random ASCII char

            print(i + 1, " ".join(word_list), "THIS LINE")
        print(i + 1, a_string)


my_string = "I will never spam my friends again"

multiply_sentence_with_typos(my_string, 50)
