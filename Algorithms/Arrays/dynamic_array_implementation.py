import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python List"""

    def __init__(self):
        """create an empty array"""
        self._n = 0  # count actual elements
        self._capacity = 1  # Default array capacity
        self._A = self._make_array(self._capacity)  # Low level array

    def __len__(self):
        """Return number of elements stored in the array"""
        return self._n

    def __getitem__(self, k):
        """Return Element at index k"""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]  # Retrieve from array

    def append(self, obj):
        """Add object to end of the array"""
        if self._n == self._capacity:  # Not enough room
            self._resize(2 * self._capacity)  # So double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):  # Non public utility
        """Resize internal array to capacity C"""
        B = self._make_array(c)  # New bigger array
        for k in range(self._n):  # for each existing value
            B[k] = self._A[k]
        self._A = B  # Use bigger array
        self._capacity = c

    def _make_array(self, c):  # Non public utility
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()  # See ctypes documentation

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        """Remove first occurance of value (or raise ValueError)"""
        for k in range(self._n):
            if self._A[k] == value:  # Found a match
                for j in range(k, self._n - 1):  # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None  # Help the garbage collector
                self._n -= 1  # We have one less item
                return  # Exit immediately
            raise ValueError('value not found')  # Only reached if no match
