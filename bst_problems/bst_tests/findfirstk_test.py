import unittest
from bst_algs.node import Node
from bst_algs.searchBST import findfirstk_iterative as ffk_it
from bst_algs.searchBST import findfirstk_recursive as ffk_rec


class TestFindFirstK(unittest.TestCase):
    """Test suite for findfirstk (iterative and recursive) on a BST."""

    def test_singleelement(self):
        """Test when there's one element."""
        root = Node(key=42)
        self.assertEqual(ffk_it(root, 42), root)
        self.assertEqual(ffk_rec(root, 42), root)

    def test_twoelements_distinct(self):
        """Test when there's two distinct elements."""
        root = Node(key=42)
        right = Node(key=50)
        root.right = right
        self.assertEqual(ffk_it(root, 42), root)
        self.assertEqual(ffk_rec(root, 50), right)

    def test_twoelements_notdistinct(self):
        """Test when there are two elements, but they're the same."""
        root = Node(key=42)
        right = Node(key=42)
        root.right = right
        self.assertEqual(ffk_it(root, 42), root)
        self.assertEqual(ffk_rec(root, 42), root)

    def test_threeelements_distinct(self):
        """Test when there's three distinct elements."""
        root = Node(key=42)
        left = Node(key=19)
        right = Node(key=52)
        root.right = right
        root.left = left
        self.assertEqual(ffk_it(root, 42), root)
        self.assertEqual(ffk_it(root, 19), left)
        self.assertEqual(ffk_it(root, 52), right)
        self.assertEqual(ffk_rec(root, 42), root)
        self.assertEqual(ffk_rec(root, 19), left)
        self.assertEqual(ffk_rec(root, 52), right)

    def test_threeelements_notdistinct(self):
        """Test when there's three elements, but they're not all distinct."""
        root = Node(key=42)
        left = Node(key=19)
        right = Node(key=42)
        root.right = right
        root.left = left
        self.assertEqual(ffk_it(root, 42), root)
        self.assertEqual(ffk_it(root, 19), left)
        self.assertEqual(ffk_rec(root, 42), root)
        self.assertEqual(ffk_rec(root, 19), left)

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
        self.assertEqual(ffk_it(A, 29), L)
        self.assertEqual(ffk_it(A, 19), B)
        self.assertEqual(ffk_it(A, 11), G)
        self.assertEqual(ffk_rec(A, 29), L)
        self.assertEqual(ffk_rec(A, 19), B)
        self.assertEqual(ffk_rec(A, 11), G)


if __name__ == "__main__":
    unittest.main()
