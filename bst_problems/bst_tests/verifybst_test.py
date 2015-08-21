import unittest
from bst_algs.verifybst import verifyBST
from bst_algs.node import Node


class TestVerifyBST(unittest.TestCase):
    """A test suite for verifyBST()."""

    def test_singleelement(self):
        """Tests single node case."""
        root = Node(key=42)
        self.assertTrue(verifyBST(root))

    def test_allequal(self):
        """Tests when all nodes have the same value."""
        left = Node(key=42, left=Node(key=42))
        right = Node(key=42, left=Node(key=42))
        root = Node(key=42, left=left, right=right)
        self.assertTrue(verifyBST(root))

    def test_singlechild(self):
        """Tests a valid 2-node tree."""
        root = Node(key=42, left=Node(key=1))
        self.assertTrue(verifyBST(root))
        root = Node(key=42, right=Node(key=43))
        self.assertTrue(verifyBST(root))

    def test_singlechild_fail(self):
        """Tests an invalid 2-node tree."""
        root = Node(key=42, left=Node(key=100))
        self.assertFalse(verifyBST(root))
        root = Node(key=42, right=Node(key=4))
        self.assertFalse(verifyBST(root))

    def test_textbook_example(self):
        """Tests the BST provided from text."""
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

        self.assertTrue(verifyBST(A))

        # Modify BST so that it is no longer valid.
        K.key = 42
        self.assertFalse(verifyBST(A))


if __name__ == "__main__":
    unittest.main()
