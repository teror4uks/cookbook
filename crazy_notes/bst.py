from crazy_notes.tqueue import CQueue


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "Data={}".format(self.data)

    def __repr__(self):
        return self.__str__()


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min_value(self):
        """
        >>> from crazy_notes.bst import BinarySearchTree
        >>> b = BinarySearchTree()
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
        >>> b.insert(5)
        True
        >>> b.insert(22)
        True
        >>> b.min_value()
        5
        """
        if self.root is None:
            return

        current = self.root.left

        while current.left is not None:
            current = current.left

        return current.data

    def max_value(self):
        """
        >>> from crazy_notes.bst import BinarySearchTree
        >>> b = BinarySearchTree()
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
        >>> b.insert(5)
        True
        >>> b.insert(22)
        True
        >>> b.max_value()
        22
        """
        if self.root is None:
            return

        current = self.root.right

        while current.right is not None:
            current = current.right

        return current.data

    def height(self):
        """
        >>> from crazy_notes.bst import BinarySearchTree
        >>> b = BinarySearchTree()
        >>> b.insert(15)
        True
        >>> b.insert(10)
        True
        >>> b.insert(18)
        True
        >>> b.insert(8)
        True
        >>> b.height()
        2
        >>> b.insert(7)
        True
        >>> b.insert(6)
        True
        >>> b.insert(5)
        True
        >>> b.height()
        5
        """
        node = self.root
        return self._height(node)

    def insert(self, data):
        """
        >>> from crazy_notes.bst import BinarySearchTree
        >>> b = BinarySearchTree()
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

    def level_order_traversal_values(self):
        """
        >>> from crazy_notes.bst import BinarySearchTree
        >>> b = BinarySearchTree()
        >>> b.insert(15)
        True
        >>> b.insert(10)
        True
        >>> b.insert(8)
        True
        >>> b.insert(12)
        True
        >>> b.level_order_traversal_values()
        [15, 10, 8, 12]
        """
        if self.root is None:
            return

        queue = CQueue()
        node = self.root
        result = []
        queue.enqueue(node)

        while not queue.is_empty():
            current = queue.front()
            result.append(current.data)

            if current.left is not None:
                queue.enqueue(current.left)

            if current.right is not None:
                queue.enqueue(current.right)

            queue.dequeue()

        return result

    def preorder(self):
        """
        >>> from crazy_notes.bst import BinarySearchTree
        >>> b = BinarySearchTree()
        >>> b.insert(15)
        True
        >>> b.insert(123)
        True
        >>> b.insert(13)
        True
        >>> b.insert(6)
        True
        >>> b.insert(125)
        True
        >>> b.preorder()
        [15, 13, 6, 123, 125]
        """
        if self.root is None:
            return

        node = self.root
        result = []
        self._preorder(node, result)

        return result

    def inorder(self):
        """
        >>> from crazy_notes.bst import BinarySearchTree
        >>> b = BinarySearchTree()
        >>> b.insert(15)
        True
        >>> b.insert(123)
        True
        >>> b.insert(13)
        True
        >>> b.insert(6)
        True
        >>> b.insert(125)
        True
        >>> b.inorder()
        [6, 13, 15, 123, 125]
        """
        if self.root is None:
            return

        node = self.root
        result = []
        self._inorder(node, result)

        return result

    def postorder(self):
        """
        >>> from crazy_notes.bst import BinarySearchTree
        >>> b = BinarySearchTree()
        >>> b.insert(123)
        True
        >>> b.add(12)
        True
        >>> b.insert(444)
        True
        >>> b.insert(23)
        True
        >>> b.postorder()
        [23, 12, 444, 123]
        >>> b.root
        Data=123
        >>> b.root.left
        Data=12
        >>> b.root.right
        Data=444
        """
        if self.root is None:
            return

        node = self.root
        result = []
        self._postorder(node, result)
        return result

    def add(self, data):
        """
        # Same as insert method just using recursion instead loop
        >>> from crazy_notes.bst import BinarySearchTree
        >>> b = BinarySearchTree()
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

    def search(self, data):
        return self._search(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return self._create_node(data)

        if data <= node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        return node

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

    def _height(self, node):
        if node is None:
            return -1

        left = self._height(node.left)
        right = self._height(node.right)
        return max(left, right) + 1

    def _inorder(self, node, result):

        if not node:
            return

        self._inorder(node.left, result)
        result.append(node.data)
        self._inorder(node.right, result)

    def _preorder(self, node, result):

        if not node:
            return

        result.append(node.data)
        self._preorder(node.left, result)
        self._preorder(node.right, result)

    def _postorder(self, node, result):

        if not node:
            return

        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(node.data)


def is_subtree_lesser(root, value):
    if root is None:
        return True

    if root.data <= value and is_subtree_lesser(root.left, value) and is_subtree_lesser(root, value):
        return True

    return False


def is_subtree_greater(root, value):
    if root is None:
        return True

    if root.data > value and is_subtree_greater(root.left, value) and is_subtree_greater(root.right, value):
        return True

    return False


def is_binary_search_tree(bst):
    root = bst.root
    if not root:
        return True

    if is_subtree_lesser(root.left, root.data) \
        and is_subtree_greater(root.right, root.value) \
        and is_binary_search_tree(root.left) \
        and is_binary_search_tree(root.right):
        return True

    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

