class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and it's successors as a string.

        >>> Node(3).as_string()
        '3'

        >>> Node(3, Node(2, Node(1))).as_string()
        '321'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)


def remove_node(node):
    """Given a node in a linked list, remove it.

    Remove this node from a linked list. Note that we do not have access to
    any other nodes of the linked list, like the head or the tail.

    Does not return anything; changes list in place.

    >>> four_node = Node(4)
    >>> three_node = Node(3, four_node)
    >>> two_node = Node(2, three_node)
    >>> one_node = Node(1, two_node)
    >>> one_node.as_string()
    '1234'
    >>> remove_node(two_node)
    >>> one_node.as_string()
    '134'

    """

    node.data = node.next.data
    node.next = node.next.next


def reverse_linked_list(head):
    """Given LL head node, return head node of new, reversed linked list.

    >>> ll = Node(1, Node(2, Node(3)))
    >>> reverse_linked_list(ll).as_string()
    '321'
    """

    new = None
    current = head
    while current:
        new = Node(current.data, new)
        current = current.next

    return new


if __name__ == "__main__":
    import doctest
    doctest.testmod()
