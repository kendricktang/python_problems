import unittest
from bst_algs.minfirst import findk
from bst_algs.node import Node


class TestFindKInMinFirst(unittest.TestCase):
    """A test suite for finding k in a min-first tree."""

    def test_singleelement(self):
        """Tests a single-element tree."""
        root = Node(key=42)
        self.assertTrue(findk(root, 42))
        self.assertFalse(findk(root, 41))

    def test_threeelements_split(self):
        """Tests three-element tree where root has two children."""
        root = Node(key=42)
        left = Node(key=50)
        right = Node(key=100)
        root.left = left
        root.right = right
        self.assertTrue(findk(root, 42))
        self.assertTrue(findk(root, 50))
        self.assertTrue(findk(root, 100))

    def test_threeelements_chain(self):
        """Tests three-element tree where root has one child."""
        root = Node(key=42)
        left = Node(key=50)
        right = Node(key=100)
        root.left = left
        left.right = right
        self.assertTrue(findk(root, 42))
        self.assertTrue(findk(root, 50))
        self.assertTrue(findk(root, 100))

    def test_testbookexample(self):
        """Tests the min-first tree from text."""
        i = Node(key=23)
        h = Node(key=19, left=i)
        g = Node(key=17)
        c = Node(key=13, left=g, right=h)

        e = Node(key=7)
        f = Node(key=11)
        d = Node(key=5, left=e, right=f)
        b = Node(key=3, right=d)

        a = Node(key=2, left=b, right=c)

        self.assertTrue(findk(a, 2))
        self.assertTrue(findk(a, 13))
        self.assertTrue(findk(a, 11))
        self.assertTrue(findk(a, 19))
        self.assertTrue(findk(a, 23))
        self.assertFalse(findk(a, 1))
        self.assertFalse(findk(a, -1))
        self.assertFalse(findk(a, 100))


if __name__ == "__main__":
    unittest.main()
