import unittest
from bst_algs.node import Node


class TestFindLargestK(unittest.TestCase):
    """A test suite for finding the largest k elements in a tree."""

    def test_singleelement(self):
        """Tests a single-element tree."""
        root = Node(key=42)
        self.assertEqual(Node.getheight(root), 0)

    def test_threeelements_split(self):
        """Tests three-element tree where root has two children."""
        root = Node(key=42, left=Node(key=10), right=Node(key=100))
        self.assertEqual(Node.getheight(root), 1)

    def test_threeelements_chain(self):
        """Tests three-element tree where root has one child."""
        root = Node(key=42)
        left = Node(key=10)
        right = Node(key=28)
        root.left = left
        left.right = right
        self.assertEqual(Node.getheight(root), 2)
        self.assertEqual(Node.getheight(left), 1)
        self.assertEqual(Node.getheight(right), 0)

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

        self.assertEqual(Node.getheight(A), 5)
        self.assertEqual(Node.getheight(K), 2)
        self.assertEqual(Node.getheight(B), 3)


if __name__ == "__main__":
    unittest.main()
