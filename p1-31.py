"""
Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.
"""


def change_due(price, amount_paid):
    """
    Calculates the amount of change due from a cost amount vs paid amount
    :param price: float
    :param amount_paid: float
    :return: float
    """
    change_required = amount_paid - price
    return change_required


def number_of_bills(change_required):
    """
    Calculates the number of bills and which bills make up the amount due
    :param change_required: float
    :return: dict
    """
    denominations = {
        50.00: 0,
        20.00: 0,
        10.00: 0,
        5.00: 0,
        2.00: 0,
        1.00: 0,
        0.50: 0,
        0.20: 0,
        0.10: 0,
        0.05: 0,
        0.02: 0,
        0.01: 0
    }
    epsilon = 0.01
    while change_required > 0 + epsilon:
        for k in denominations.keys():  # Cycle through the keys of the dictionary
            while change_required >= k:  # If the key is still deductible, take it again
                if k <= change_required:
                    denominations[k] += 1
                    change_required -= k
    return denominations


def format_values(denominations):
    """
    Formats the dict given and prints the bills required
    :param denominations:
    :return: format string
    """
    for k in denominations:
        print(f"£{k:.2f} * {denominations[k]}")


def main():
    price = float(input("What is the cost of the item? "))
    money_given = float(input("How much money are you giving me? "))
    change = change_due(price, money_given)
    print(f"Change Due: {change:.2f}")
    denom_due = number_of_bills(change)
    format_values(denom_due)


if __name__ == '__main__':
    main()
