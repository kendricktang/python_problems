import unittest
from bst_algs.BSTtox import BSTtolinkedlist as BSTtoLL
from bst_algs.node import Node


class TestBSTtoLinkedList(unittest.TestCase):
    """A test suite for converting a BST to a linked list."""

    def test_singleelement(self):
        """Tests a single-element tree."""
        root = Node(key=42)

        ll = BSTtoLL(root)
        sort, count = issorted(ll)
        self.assertTrue(sort)
        self.assertEqual(count, 1)

    def test_threeelements_split(self):
        """Tests three-element tree where root has two children."""
        root = Node(key=42, left=Node(key=10), right=Node(key=100))

        ll = BSTtoLL(root)
        sort, count = issorted(ll)
        self.assertTrue(sort)
        self.assertEqual(count, 3)

    def test_threeelements_chain(self):
        """Tests three-element tree where root has one child."""
        root = Node(key=42)
        left = Node(key=10)
        right = Node(key=28)
        root.left = left
        left.right = right

        ll = BSTtoLL(root)
        sort, count = issorted(ll)
        self.assertTrue(sort)
        self.assertEqual(count, 3)

    def test_testbookexample(self):
        """Tests the tree from text."""
        C = Node(key=3, left=Node(key=2), right=Node(key=5))
        G = Node(key=17, left=Node(key=13))
        F = Node(key=11, right=G)
        B = Node(key=7, left=C, right=F)

        L = Node(key=29, right=Node(key=31))
        K = Node(key=37, left=L, right=Node(key=41))
        J = Node(key=23, right=K)
        O = Node(key=47, right=Node(key=53))
        I = Node(key=43, left=J, right=O)
        A = Node(key=19, left=B, right=I)

        ll = BSTtoLL(A)
        sort, count = issorted(ll)
        self.assertTrue(sort)
        self.assertEqual(count, 16)


def issorted(ll):
    count = 0
    while ll and ll.right:
        count += 1
        if ll.key > ll.right.key:
            return False, -1
        ll = ll.right
    return True, count+1


if __name__ == "__main__":
    unittest.main()
