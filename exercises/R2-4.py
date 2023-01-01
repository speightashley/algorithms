"""
Write a Python class, Flower, that has three instance variables of type str,
int, and ﬂoat, that respectively represent the name of the ﬂower, its num-
ber of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.

"""


class Flower:

    def __init__(self, name, num_petals, price):
        self._name = name
        self._num_petals = num_petals
        self._price = price

    def get_name(self):
        return self._name

    def set_name(self, x):
        self._name = x

    def get_num_petals(self):
        return self._num_petals

    def set_num_petals(self, x):
        self._num_petals = x

    def get_price(self):
        return self._price

    def set_price(self, x):
        self._price = x


my_flower = Flower('rose', 5, 2.99)

print(my_flower.get_name())

my_flower.set_name("dandelion")

print(my_flower.get_name())

print(my_flower.get_price())


