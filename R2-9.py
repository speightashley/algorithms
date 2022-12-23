"""
Implement the sub method for the Vector class of Section 2.3.3, so
that the expression u−v returns a new vector instance representing the
difference between two vectors.
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

