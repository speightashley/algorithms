class Progression:
    """Iterator producing a generic progression

    Default iterator produces the whole numbers 0, 1, 2
    """

    def __init__(self, start=0):
        """Initiate current to the first value of the progression"""

        self._current = start

    def _advance(self):
        """Update self._current to a new value

        This should be overridden by a subclass to customise progression

        By convention, if current is set to None, this designates the end of a finite progression

        """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error"""
        if self._current is None:  # Our convention to end the progression
            raise StopIteration()
        else:
            answer = self._current  # Record current value to return
            self._advance()  # Advance to prepare for next time
            return answer  # Return the answer

    def __iter__(self):
        """By convention an iterator must return itself as an iterator"""
        return self

    def print_progression(self, n):
        """print next n values of the progression"""
        print(" ".join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):  # Inherited from progression class
    """Iterator producing an arithmetic progression"""

    def __init__(self, increment=1, start=0):
        """create a new arithmetic progression

        Increment the fixed constant to add to each term (default 1)
        start  the first term of the progression (default 0)

        """
        super().__init__(start)  # Initialise base class
        self._increment = increment

    def _advance(self):  # Override inherited version
        """Update current value by adding the fixed increment"""
        self._current += self._increment


class GeometricProgression(Progression):  # Inherit from Progression
    """Iterator producing a geometric progression"""

    def __init__(self, base=2, start=0):
        """Create a new geometric progression

        base - The fixed constant multiplied to each term(default 2)
        start - The first term of the progression (default 1)
        """
        super().__init__(start)
        self._base = base

    def _advance(self):  # Override inherited version
        """Update current value by multiplying it by the base value"""
        self._current *= self._base
