class Stack:
    """
    >>> from crazy_notes.stack import Stack
    >>> s = Stack()
    >>> s.push(1)
    >>> s.push(2)
    >>> s.push(3)
    >>> s.top()
    3
    >>> s.is_empty()
    False
    >>> s.pop()
    3
    >>> s.top()
    2
    """
    def __init__(self, max_size=101):
        self.elements = [None] * max_size
        self.top_element = -1
        self.max_size = max_size

    def top(self):
        if self.is_empty():
            return

        return self.elements[self.top_element]

    def pop(self):
        if self.is_empty():
            return

        el = self.top()
        self.top_element -= 1
        return el

    def push(self, element):
        if self.top_element >= self.max_size -1:
            raise Exception('Stack is overflow')

        self.top_element += 1
        self.elements[self.top_element] = element

    def is_empty(self):
        if self.top_element == -1:
            return True

        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
