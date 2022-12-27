"""
You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove
the letter at that index from word so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false
otherwise.

Note:

    The frequency of a letter x is the number of times it occurs in the string.
    You must remove exactly one letter and cannot chose to do nothing.


"""


def equalFrequency(word: str) -> bool:
    empty_dict = {}
    for i in range(len(word)):
        empty_dict[word[i]] = empty_dict.get(word[i], 0) + 1

    list = [1, 2, 3, 5, 6]
    target = 4

    if target in list:
        return list.index(target)
    else:
        list = list.append(target)
        list = sorted(list)
        return list.index(target)







equalFrequency("aabbccddd")
