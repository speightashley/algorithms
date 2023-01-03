class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class ArrayStack:
    """
    Lifo stack implementation using Python list as underlying storage
    """

    def __init__(self):
        """
        Create an empty stack
        """
        self._data = []  # Non-public list instance

    def __len__(self):
        """Return number of Elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """ Add an element to the stack"""
        self._data.append(e)  # New item stored at the end of a list

    def top(self):
        """Return the last element on the stack"""
        if self.is_empty():
            raise Empty("stack is empty")
        return self._data[-1]  # The last item at the end of the stack

    def pop(self):
        """Remove and return the element form the top of the stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()  # Remove last item from the stack

