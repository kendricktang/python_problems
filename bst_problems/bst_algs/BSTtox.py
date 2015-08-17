def BSTtolinkedlist(root):
    """Converts a BST to a cyclically doubly linked list,
    where the doubly linked list is represented by a BST node.
    Left child is equivalent to parent pointer.
    Right child is equivalent to next pointer.
    The beginning of the list has a parent pointer to the end of the list."""

    if not root:
        return None

    left_front = BSTtolinkedlist(root.left)
    right_front = BSTtolinkedlist(root.right)

    # Append left list
    if left_front:
        left_end = left_front.left
        left_end.right = root
        root.left = left_end
    else:
        left_front = root
        left_front.left = left_front

    left_end = root

    # Append right list
    if right_front:
        right_end = right_front.left
        left_end.right = right_front
        right_front.left = left_end
        left_end = right_end

    # Make it cyclical again and return the front of the list.
    left_end.right = left_front
    return left_front


if __name__ == "__main__":
    from numpy import random
    from node import Node

    random.seed(0)
    size = 500
    testsize = 200
    for ind in xrange(testsize):
        bst = Node()
        for x in xrange(size):
            bst.add(Node(key=random.randint(-100, 100)))
        linkedlist = BSTtolinkedlist(bst)
        curr = linkedlist
        while curr and curr.right != linkedlist:
            if curr.key > curr.right.key:
                print "fail."
            curr = curr.right
