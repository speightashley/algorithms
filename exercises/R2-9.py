"""
Implement the sub method for the Vector class of Section 2.3.3, so
that the expression u−v returns a new vector instance representing the
difference between two vectors.

Implement the neg method for the Vector class of Section 2.3.3, so
that the expression −v returns a new vector instance whose coordinates
are all the negated values of the respective coordinates of v

R-2.11 In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
Explain how the Vector class deﬁnition can be revised so that this syntax
generates a new vector.

R-2.12 Implement the mul method for the Vector class of Section 2.3.3, so
that the expression v 3 returns a new vector with coordinates that are 3
times the respective coordinates of v.

R-2.13 Exercise R-2.12 asks for an implementation of mul , for the Vector
class of Section 2.3.3, to provide support for the syntax v 3. Implement
the rmul method, to provide additional support for syntax 3 v.
"""


class Vector:

    def __init__(self, d):
        if isinstance(d, list):
            self._coords = [0] * len(d)
            for x in range(len(d)):
                self._coords[x] = d[x]
        else:
            self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return not self == other

    def __str__(self):
        return "<" + str(self._coords)[1: -1] + ">"

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for value in range(len(self)):
            result[value] = -abs(self[value])
        return result

    def __mul__(self, x):
        result = Vector(len(self))
        for num in range(len(self)):
            result[num] = self[num] * x
        return result

    def __rmul__(self, x):
        result = Vector(len(self))
        for num in range(len(self)):
            result[num] = self[num] * x
        return result


my_vector = Vector(3)
my_other_vector = Vector(3)

my_vector[0] = 60
my_vector[1] = 170
my_vector[2] = 250

my_other_vector[0] = 27
my_other_vector[1] = 130
my_other_vector[2] = 200

new_vector = my_vector - my_other_vector

for i in range(len(new_vector)):
    print(new_vector[i])

print(new_vector)

print(new_vector * 5)
print(5 * new_vector)

my_latest_vector = Vector(5)

print(my_latest_vector)
