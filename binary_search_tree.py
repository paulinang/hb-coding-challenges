class Node(object):  # ...
    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def insert(self, new_data):
        """ Insert new node with `new_data` to BST tree rooted here.
        >>> t = Node(4,
        ...       Node(2, Node(1), Node(3)),
        ...       Node(7, Node(5), Node(8))
        ... )

        >>> t.insert(0)

        >>> t.left.left.left.data == 0
        True

        >>> t.left.left.right is None
        True

        >>> t.insert(9)

        >>> t.right.right.right.data == 9
        True

        >>> t.right.right.left is None
        True

        >>> t.insert(6)

        >>> t.right.left.right.data == 6
        True

        >>> t.right.left.left is None
        True
        """

        if new_data < self.data:
            if self.left:
                self.left.insert(new_data)
            else:
                self.left = Node(new_data)
        else:
            if self.right:
                self.right.insert(new_data)
            else:
                self.right = Node(new_data)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
