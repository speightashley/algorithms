"""
Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
"""


def read_input(filename):
    file = open(filename)
    lines = []
    while True:
        try:
            line = file.readline()
            if line == '':
                raise EOFError
            lines.append(line)
        except EOFError:
            for line in reversed(lines):
                print(line, end='')
            file.close()
            return


read_input('../text.txt')
