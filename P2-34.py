"""

Write a Python program that inputs a document and then outputs a bar-
chart plot of the frequencies of each alphabet character that appears in
that document

"""

import matplotlib.pyplot as plt

filename = "text.txt"

file1 = open(filename, 'r')

word_frequency = {}

for words in file1:
    for letters in words:
        word_frequency[letters] = word_frequency.get(letters, 0) + 1

plt.bar(range(len(word_frequency)), list(word_frequency.values()), align='center')
plt.xticks(range(len(word_frequency)), list(word_frequency.keys()))
plt.show()
