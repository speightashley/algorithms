class Empty(Exception):
    pass


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage"""

    class _Node:
        """Class for data storage in singly linked list"""

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty queue"""
        self._head = None
        self._tail = None
        self._size = 0  # Number of queue elements

    def __len__(self):
        """size of the queue"""
        return self._size

    def is_empty(self):
        """Return True if empty or False if not"""
        return self._size == 0

    def first(self):
        """Return the first element in the queue"""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element  # Front aligned with head of list

    def dequeue(self):
        """pop off and return the first element in the queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():  # Special case as queue is empty
            self._tail = None  # Removed head had been the tail
        return answer

    def enqueue(self, e):
        """Add a new element to the queue"""
        newest = self._Node(e, None)  # Node will be new tail node
        if self.is_empty():
            self._head = newest  # Special case, previously empty
        else:
            self._tail = newest
        self._tail = newest  # Update reference to tail node
        self._size += 1
