"""

Use the techniques of Section 1.7 to revise the charge and make payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter.

If the parameter to the make payment method of the CreditCard class
were a negative number, that would have the effect of raising the balance
on the account. Revise the implementation so that it raises a ValueError if
a negative value is sent.

R-2.7 The CreditCard class of Section 2.3 initializes the balance of a new ac-
count to zero. Modify that class so that a new account can be given a
nonzero balance using an optional ﬁfth parameter to the constructor. The
four-parameter constructor syntax should continue to produce an account
with zero balance.

R-2.8 Modify the declaration of the ﬁrst for loop in the CreditCard tests, from
Code Fragment 2.3, so that it will eventually cause exactly one of the three
credit cards to go over its credit limit. Which credit card is it?

"""


class CreditCard:

    def __init__(self, customer, bank, account, limit, balance=0):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("price must be numeric")
        elif price < 0:
            raise ValueError("Price can't be negative")
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be numeric")
        elif amount < 0:
            raise ValueError("Amount must be positive")
        self._balance -= amount


if __name__ == '__main__':
    wallet = [CreditCard('John Bowman', 'California Savings',
                         '5391 0375 9387 5309', 2500), CreditCard('John Bowman', 'California Federal',
                                                                          '3485 0399 3395 1954', 3500),
              CreditCard('John Bowman', 'California Finance',
                         '5391 0375 9387 5309', 5000)]

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        print()
