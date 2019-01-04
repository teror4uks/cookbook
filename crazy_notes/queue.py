

class Queue:
    """
    >>> from crazy_notes.queue import Queue
    >>> q = Queue()
    >>> q.is_empty()
    True
    >>> q.is_full()
    False
    >>> q.dequeue()
    False
    >>> [q.enqueue(i) for i in range(11)]
    [True, True, True, True, True, True, True, True, True, True, False]
    >>> q.front()
    0
    >>> q.rear()
    9
    >>> q.dequeue()
    True
    >>> q.front()
    1
    >>> q.enqueue(20)
    True
    >>> q.rear()
    20
    """
    def __init__(self, size=10):
        self.queue = [None] * size
        self._front = -1
        self._rear = -1
        self.max_size = size

    def is_empty(self):
        return self._front == -1 and self._rear == -1

    def is_full(self):
        return self._rear == self.max_size - 1

    def enqueue(self, item):
        if (self._rear + 1) % self.max_size == self._front:
            return False

        elif self.is_empty():
            self._front = self._rear = 0
        else:
            self._rear = (self._rear + 1) % self.max_size

        self.queue[self._rear] = item

        return True

    def dequeue(self):
        if self.is_empty():
            return False

        if self._front == self._rear:
            self._front = self._rear = -1
            return True

        self._front = (self._front + 1) % self.max_size

        return True

    def front(self):
        return self.queue[self._front]

    def rear(self):
        return self.queue[self._rear]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
