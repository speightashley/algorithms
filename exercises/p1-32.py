"""
Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
"""


def calc(x, op, y):
    """
    Takes in two floats and an operator to return an answer
    :param x: float
    :param op: operator
    :param y: float
    :return: float
    """

    match op:
        case "+":
            return x + y
        case "-":
            return x - y
        case "/":
            return x / y
        case "*":
            return x * y
        case _:
            print("Error")
            return 0


def main():
    import operator
    # Take input from user for first digit
    x = float(input("1st number "))
    op = input("What operation? ")  # Get the operator
    y = float(input("What second number? "))  # Get the second number

    print(calc(x, op, y))


main()
