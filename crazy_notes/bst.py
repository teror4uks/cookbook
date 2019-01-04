class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "Data={}".format(self.data)

    def __repr__(self):
        return self.__str__()


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        >>> from crazy_notes.bst import BinaryTree
        >>> b = BinaryTree()
        >>> b.insert(15)
        True
        >>> b.insert(10)
        True
        >>> b.insert(8)
        True
        >>> b.insert(12)
        True
        >>> b.insert(17)
        True
        """
        new_node = self._create_node(data)

        if self.root is None:
            self.root = new_node
            return True

        elif data <= self.root.data:
            node = self.root.left

            if not node:
                self.root.left = new_node
                return True

        else:
            node = self.root.right
            if not node:
                self.root.right = new_node
                return True

        while node:
            if node.data >= data:
                if not node.left:
                    node.left = new_node
                    return True

                node = node.left

            else:
                if not node.right:
                    node.right = new_node
                    return True

                node = node.right

        return False

    def add(self, data):
        """
        # Same as insert method just using recursion instead loop
        >>> from crazy_notes.bst import BinaryTree
        >>> b = BinaryTree()
        >>> b.add(15)
        True
        >>> b.add(10)
        True
        >>> b.add(8)
        True
        >>> b.add(12)
        True
        >>> b.add(17)
        True
        """
        if self.root is None:
            self.root = self._create_node(data)
            return True

        return True if self._insert(self.root, data) else False

    def _insert(self, node, data):
        if node is None:
            return self._create_node(data)

        if data <= node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        return node

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True

        if data <= node.data:
            return self._search(node.left, data)

        return self._search(node.right, data)

    @staticmethod
    def _create_node(data, left=None, right=None):
        return Node(data, left, right)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
