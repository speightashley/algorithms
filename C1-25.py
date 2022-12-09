"""
Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For exam-
ple, if given the string "Let s try, Mike.", this function would return
"Lets try Mike".
"""


def punc_strip(s):
    import string
    new_string = s.translate(str.maketrans('', '', string.punctuation))  # Punctuation() comes from the String module
    return new_string


print(punc_strip("This is a sentence, it's got punctuation ? "))
