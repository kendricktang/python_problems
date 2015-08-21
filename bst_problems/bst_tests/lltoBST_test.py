import unittest
from bst_algs.xtoBST import linkedlisttoBST as lltoBST
from bst_algs.verifybst import verifyBST as verify
from bst_algs.node import Node
from math import ceil, log


class TestLinkedListToBST(unittest.TestCase):
    """A test suite for converting a linked list to a BST of minimal height."""

    def test_null(self):
        """Tests a null linked list."""
        linkedlist = None
        bst = lltoBST(linkedlist)
        self.assertTrue(verify(bst))
        self.assertTrue(Node.getheight(bst) == -1)

    def test_singleelement(self):
        """Tests a linked list with one element."""
        linkedlist = Node(key=42)
        bst = lltoBST(linkedlist)
        self.assertTrue(verify(bst))
        self.assertTrue(Node.getheight(bst) <= ceil(log(1, 2)))

    def test_twoelements(self):
        """Tests a linked list with two elements."""
        linkedlist = Node(key=10, right=Node(key=42))
        bst = lltoBST(linkedlist)
        self.assertTrue(verify(bst))
        self.assertTrue(Node.getheight(bst) <= ceil(log(2, 2)))

    def test_threeelements(self):
        """Tests a linked list with three elements."""
        linkedlist = Node(key=10, right=Node(key=42, right=Node(key=100)))
        bst = lltoBST(linkedlist)
        self.assertTrue(verify(bst))
        self.assertTrue(Node.getheight(bst) <= ceil(log(3, 2)))

    def test_oneelementss(self):
        """Tests a linked list with only one key."""
        array = [42, 42, 42, 42, 42, 42, 42, 42]
        linkedlist = arraytolinkedlist(array)
        bst = lltoBST(linkedlist)
        self.assertTrue(verify(bst))
        self.assertTrue(Node.getheight(bst) <= ceil(log(len(array), 2)))

    def test_testbookexample(self):
        """Tests an array containing keys from the tree from text."""
        array = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
        linkedlist = arraytolinkedlist(array)
        bst = lltoBST(linkedlist)
        self.assertTrue(verify(bst))
        self.assertTrue(Node.getheight(bst) <= ceil(log(len(array), 2)))


def arraytolinkedlist(array):
    """Converts an array into a linked list."""
    if not array:
        return None

    ret = Node(key=array[0])
    curr = ret
    for ele in array[1:]:
        curr.right = Node(key=ele)
        curr = curr.right
    return ret


if __name__ == "__main__":
    unittest.main()
