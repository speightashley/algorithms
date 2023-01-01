"""
Give a short fragment of Python code that uses the progression classes
from Section 2.4.2 to ﬁnd the 8th value of a Fibonacci progression that
starts with 2 and 2 as its ﬁrst two values

"""


class Progression:
    """
    Iterator producing a generic progression

    Default iterator produces the whole numbers 0, 1, 2, ...

    """

    def __init__(self, start=0):
        """initialise current to the first value of the progression"""
        self._current = start

    def _advance(self):
        """
        Update self._current to a new value

        This should be overridden by a subclass to customize progression.

        By convention, if current is set to None, this designates the end of a finite progression

        """

        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error"""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """by convention an iterator must return itself as an iterator"""
        return self

    def print_progression(self, n):
        """Print next n values of the progression"""
        print(" ".join(str(next(self)) for j in range(n)))


class FibonacciProgression(Progression):
    """Iterator producing a generalised Fibonacci progression"""

    def __init__(self, first=0, second=1):
        """create a new fibonacci progression """
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current


my_progression = FibonacciProgression()

print(my_progression.print_progression(80))
