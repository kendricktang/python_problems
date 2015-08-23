import unittest
from bst_algs.findsuccessor import findsuccessor
from bst_algs.node import Node


class TestFindSuccessor(unittest.TestCase):
    """A test suite for findsuccessor()."""

    def test_singleelement(self):
        """Tests when there is only one element. No successor here."""
        root = Node(key=42)
        self.assertEqual(findsuccessor(root), None)

    def test_threeelements(self):
        """Tests when there are three elements."""
        root = Node(key=42)
        left = Node(key=0, parent=root)
        right = Node(key=50, parent=root)
        root.left = left
        root.right = right
        self.assertEqual(findsuccessor(left), root)
        self.assertEqual(findsuccessor(root), right)
        self.assertEqual(findsuccessor(right), None)

    def test_textbooktree(self):
        """Tests the tree provided by the textbook."""
        A = Node(key=19)
        B = Node(key=7, parent=A)
        I = Node(key=43, parent=A)
        A.left = B
        A.right = I

        C = Node(key=3, parent=B)
        F = Node(key=11, parent=B)
        B.left = C
        B.right = F

        D = Node(key=2, parent=C)
        E = Node(key=5, parent=C)
        C.left = D
        C.right = E

        G = Node(key=17, parent=F)
        F.right = G

        H = Node(key=13, parent=G)
        G.left = H

        J = Node(23, parent=I)
        O = Node(47, parent=I)
        I.left = J
        I.right = O

        K = Node(key=37, parent=J)
        J.right = K

        L = Node(key=29, parent=K)
        N = Node(key=41, parent=K)
        K.left = L
        K.right = N

        M = Node(key=31, parent=L)
        L.right = M

        P = Node(key=53, parent=O)
        O.right = P

        self.assertEqual(findsuccessor(P), None)
        self.assertEqual(findsuccessor(G), A)
        self.assertEqual(findsuccessor(A), J)


if __name__ == "__main__":
    unittest.main()
