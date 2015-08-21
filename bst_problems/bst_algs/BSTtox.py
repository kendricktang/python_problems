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

    # Append left list with root
    if left_front:
        left_end = left_front.left
        left_end.right = root
        root.left = left_end
    else:
        left_front = root

    left_front.left = root
    left_end = root

    # Append right list
    if right_front:
        left_front.left = right_front.left
        left_end.right = right_front
        right_front.left = left_end

    return left_front
