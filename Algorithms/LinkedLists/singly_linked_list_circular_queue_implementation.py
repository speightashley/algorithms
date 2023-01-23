class Empty(Exception):
    pass


class CircularQueue:
    """Queue implementation using circulaly linked list for storage"""

    class _Node:
        """Lightweight, non public class for storing a singly linked node"""

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty queue"""
        self._tail = None  # Will represent tail of queue
        self._size = 0  # number of queue elements

    def __len__(self):
        """Return length of queue"""
        return self._size

    def is_empty(self):
        """Return True if empty, False if not"""
        return self._size == 0

    def first(self):
        """Return the first element in the queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        head = self._tail._next
        return head._element

    def dequeue(self):
        """Remove and return the first element"""
        if self.is_empty():
            raise Empty("Nothing in the queue")
        oldhead = self._tail._next
        if self._size == 1:  # Removing only element
            self._tail = None  # Queue becomes empty
        else:
            self._tail._next = oldhead._next  # Bypass the old head
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        """Add an element to the back of the queue"""
        newest = self._Node(e, None)  # Node will be the new tail node
        if self.is_empty():
            newest._next = newest  # Initialise circulaly
        else:
            newest._next = self._tail._next  # New node points to head
            self._tail._next = newest  # old tail points to new node
        self._tail = newest
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue"""
        if self._size > 0:
            self._tail = self._tail._next  # Old head becomes new tail
