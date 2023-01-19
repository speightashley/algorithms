class LinkedStack:
    """LIFO stack implementation using a singly linked list for storage"""

    # ------------------Nested Node Class -------------------------------------

    class _Node:
        """Lightweight, nonpublic class for storing singly linked node"""
        __slots__ = "_element", "_next"  # Streamline memory usage

        def __init__(self, element, next):  # Init nodes fields
            self._element = element  # Reference to users element
            self._next = next  # Reference to next node

    # ---------------- Stack Methods -------------------------------------------

    def __init__(self):
        """Create an empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack"""
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Return but don't remove the element at the top of the stack

        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise ("stack is empty")
        return self._head._element

    def pop(self):
        """Remove and return the element from the top of the stack LIFO"""
        if self.is_empty():
            raise ("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
