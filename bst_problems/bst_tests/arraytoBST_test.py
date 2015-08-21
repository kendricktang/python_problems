import unittest
from bst_algs.xtoBST import arraytoBST as atoBST
from bst_algs.verifybst import verifyBST as verify
from bst_algs.node import Node
from math import ceil, log


class TestArrayToBST(unittest.TestCase):
    """A test suite for converting an array to a BST of minimal height."""

    def test_null(self):
        """Tests a null tree."""
        array = []
        bst = atoBST(array)
        self.assertTrue(verify(bst))
        self.assertTrue(Node.getheight(bst) == -1)

    def test_singleelement(self):
        """Tests a single-element tree."""
        array = [42]
        bst = atoBST(array)
        self.assertTrue(verify(bst))
        self.assertTrue(Node.getheight(bst) <= ceil(log(len(array), 2)))

    def test_twoelements(self):
        """Tests 2-element array."""
        array = [10, 42]
        bst = atoBST(array)
        self.assertTrue(verify(bst))
        self.assertTrue(Node.getheight(bst) <= ceil(log(len(array), 2)))

    def test_threeelements(self):
        """Tests 3-element array."""
        array = [10, 42, 100]
        bst = atoBST(array)
        self.assertTrue(verify(bst))
        self.assertTrue(Node.getheight(bst) <= ceil(log(len(array), 2)))

    def test_oneelementss(self):
        """Tests an array with only one key."""
        array = [42, 42, 42, 42, 42, 42, 42, 42]
        bst = atoBST(array)
        self.assertTrue(verify(bst))
        self.assertTrue(Node.getheight(bst) <= ceil(log(len(array), 2)))

    def test_testbookexample(self):
        """Tests an array containing keys from the tree from text."""
        array = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
        bst = atoBST(array)
        self.assertTrue(verify(bst))
        self.assertTrue(Node.getheight(bst) <= ceil(log(len(array), 2)))


if __name__ == "__main__":
    unittest.main()
