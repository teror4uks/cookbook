class LinkedNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "{}".format(self.data)

    def __repr__(self):
        return self.__str__()


class LinkedList:
    """
    >>> from link_list import LinkedList
    >>> l = LinkedList()
    >>> [l.add(i) for i in range(10)]
    [None, None, None, None, None, None, None, None, None, None]
    >>> print(l)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> l.insert(100, 4)
    >>> print(l)
    [1, 2, 3, 4, 100, 6, 7, 8, 9]
    >>> l.delete(3)
    >>> print(l)
    [1, 2, 3, 100, 6, 7, 8, 9]
    """

    def __init__(self):
        self.head = LinkedNode()

    def add(self, data):
        node = LinkedNode(data)

        if not self.head.next and not self.head.data:
            self.head = node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = node

    def insert(self, data, index=None):
        if index is None:
            self.add(data)
            return

        new_node = LinkedNode(data)

        if index == 0:
            h_next = self.head.next
            self.head = new_node
            self.head.next = h_next
            return

        node = self.head

        for i in range(index-1):
            node = node.next

        new_node.next = node.next.next

        node.next = new_node

    def iterate(self):
        node = self.head

        while node.next:
            yield node
            node = node.next

        yield node

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            return

        node = self.head

        for i in range(index-1):
            node = node.next

        deleted_node = node.next
        node_after_deleted = deleted_node.next
        node.next = node_after_deleted

    def __str__(self):
        return "{}".format(list(self.iterate()))


class PLinkedList:
    """
    >>> from link_list import PLinkedList
    >>> pl = PLinkedList()
    >>> [pl.add(i) for i in range(10)]
    [None, None, None, None, None, None, None, None, None, None]
    >>> print(pl)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> pl[4] = 100
    >>> print(pl)
    [1, 2, 3, 4, 100, 6, 7, 8, 9]
    >>> pl.delete(3)
    >>> print(pl)
    [1, 2, 3, 100, 6, 7, 8, 9]
    """
    def __init__(self):
        self.head = LinkedNode()

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise Exception('Index must be int')

        new_node = LinkedNode(value)

        if index == 0:
            h_next = self.head.next
            self.head = new_node
            self.head.next = h_next
            return

        node = self.head

        for i in range(index - 1):
            node = node.next

        new_node.next = node.next.next

        node.next = new_node

    def __iter__(self):
        node = self.head

        while node.next:
            yield node
            node = node.next

        yield node

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            return

        node = self.head

        for i in range(index-1):
            node = node.next

        deleted_node = node.next
        node_after_deleted = deleted_node.next
        node.next = node_after_deleted

    def add(self, data):
        node = LinkedNode(data)

        if not self.head.next and not self.head.data:
            self.head = node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = node

    def __str__(self):
        return '{}'.format(list(self))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
