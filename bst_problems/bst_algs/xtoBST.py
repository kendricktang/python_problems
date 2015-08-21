from verifybst import verifyBST
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
    """Recursive helper to build BST from a sorted linked list in O(n)."""
    if start < end:
        middle = (start + end) / 2

        # Recursively do left branch
        left, linkedlist = _linkedlisttoBST(linkedlist, start, middle)

        # Do self, and pop off the top of the linked list.
        curr = linkedlist
        curr.left = left
        linkedlist = linkedlist.right

        # Recursively do right branch
        curr.right, linkedlist = _linkedlisttoBST(linkedlist, middle + 1, end)

        return curr, linkedlist
    return None, linkedlist


if __name__ == "__main__":
    from math import log, ceil
    from numpy import random

    random.seed(0)

    # Test array -> BST
    testsize = 100
    for ind in xrange(testsize):
        size = random.randint(0, 500)
        array = []
        for x in xrange(size):
            key = random.randint(-100, 100)
            array += [key]
        array.sort()
        root = arraytoBST(array)
        if not verifyBST(root):
            print "FAIL (arraytoBST): not valid tree."
        if array:
            if Node.getheight(root) > ceil(log(len(array), 2)):
                print "FAIL (arraytoBST): not min height"
        else:
            if root:
                print "FAIL (arraytoBST): should be none."

    # Test linkedlist -> BST
    for ind in xrange(testsize):
        size = random.randint(0, 500)
        array = []
        for x in xrange(size):
            key = random.randint(-100, 100)
            array += [key]
        array.sort()
        linkedlist = Node()
        for key in array:
            node = Node(key)
            linkedlist.add(node)
        root = linkedlisttoBST(linkedlist)
        if not verifyBST(root):
            print "FAIL (linkedlisttoBST): not valid tree."
        if array:
            if Node.getheight(root) > ceil(log(len(array), 2)):
                print "FAIL (linkedlisttoBST): not min height"
        else:
            if root:
                print "FAIL (linkedlisttoBST): should be None."
