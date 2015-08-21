from node import Node


def arraytoBST(array):
    """Convert a sorted array into a minimum height BST."""
    if not array:
        return None

    middle = len(array) / 2
    node = Node(key=array[middle])
    node.left = arraytoBST(array[:middle])
    node.right = arraytoBST(array[middle+1:])
    return node


def linkedlisttoBST(linkedlist):
    """Convert a sorted linked list into a minimum height BST in O(n) time.
    In this context, a linked list is a BST with only right children."""
    # Determine length of linked list (O(n)):
    length = 0
    curr = linkedlist
    while curr:
        length += 1
        curr = curr.right

    # Recursively build tree:
    root, linkedlist = _linkedlisttoBST(linkedlist, 0, length)
    return root


def _linkedlisttoBST(linkedlist, start, end):
    if start < end:
        middle = (start + end) / 2

        # Do left branch
        left, linkedlist = _linkedlisttoBST(linkedlist, start, middle)

        # Do self
        curr = linkedlist
        curr.left = left
        linkedlist = linkedlist.right

        # Do right branch
        curr.right, linkedlist = _linkedlisttoBST(linkedlist, middle + 1, end)

    return None, linkedlist
