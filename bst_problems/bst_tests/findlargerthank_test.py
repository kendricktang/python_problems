import unittest
from bst_algs.node import Node
from bst_algs.searchBST import findlargerthank as fltk


class TestFindFirstK(unittest.TestCase):
    """Test suite for findlargerthank on a BST."""

    def test_singleelement(self):
        """Test when there's one element."""
        root = Node(key=42)
        self.assertEqual(fltk(root, 42), None)

    def test_twoelements_distinct(self):
        """Test when there's two distinct elements."""
        root = Node(key=42)
        right = Node(key=50)
        root.right = right
        self.assertEqual(fltk(root, 42), right)

    def test_twoelements_notdistinct(self):
        """Test when there are two elements, but they're the same."""
        root = Node(key=42)
        right = Node(key=42)
        root.right = right
        self.assertEqual(fltk(root, 42), None)

    def test_threeelements_distinct(self):
        """Test when there's three distinct elements."""
        root = Node(key=42)
        left = Node(key=19)
        right = Node(key=52)
        root.right = right
        root.left = left
        self.assertEqual(fltk(root, 42), right)
        self.assertEqual(fltk(root, 19), root)
        self.assertEqual(fltk(root, 52), None)

    def test_threeelements_notdistinct(self):
        """Test when there's three elements, but they're not all distinct."""
        root = Node(key=42)
        left = Node(key=19)
        right = Node(key=42)
        root.right = right
        root.left = left
        self.assertEqual(fltk(root, 42), None)
        self.assertEqual(fltk(root, 19), root)

    def test_testbookexample(self):
        """Tests a modified version of the tree from text."""
        C = Node(key=19)
        G = Node(key=11, left=Node(key=10))
        F = Node(key=11, left=G)
        B = Node(key=19, left=F, right=C)

        L = Node(key=29, right=Node(key=31))
        K = Node(key=37, left=L, right=Node(key=41))
        J = Node(key=23, right=K)
        O = Node(key=47, right=Node(key=53))
        I = Node(key=43, left=J, right=O)
        A = Node(key=19, left=B, right=I)
        self.assertEqual(fltk(A, 29), L.right)
        self.assertEqual(fltk(A, 19), J)
        self.assertEqual(fltk(A, 11), B)


if __name__ == "__main__":
    unittest.main()
