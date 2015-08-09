import unittest
from bintree_algs.binarytree2 import BinaryTreeNode2 as BTN
from bintree_algs.makebintree import makefromstring as mfs


class TestPreOrderTraversal(unittest.TestCase):
    """Test suite for BinaryTreeNode.preordertraversal()."""

    def test_singlecase(self):
        """Test a tree with just a root."""
        s = "42"
        root = mfs(s, BTN)
        self.assertEqual(
            root.preordertraversal(),
            "42")

    def test_rightonly(self):
        """Test a tree with only a right side."""
        s = "42[-100(12(10)[11(17)])[32]]"
        root = mfs(s, BTN)
        self.assertEqual(
            root.preordertraversal(),
            "42,-100,12,10,11,17,32")

    def test_leftonly(self):
        """Test a tree with only a left side."""
        s = "42(-100(12(10)[11[17]])[23])"
        root = mfs(s, BTN)
        self.assertEqual(
            root.preordertraversal(),
            "42,-100,12,10,11,17,23")

    def test_bothchildren(self):
        """Test a tree which has both children."""
        s = "42(-100(12)[28])[100[111]]"
        root = mfs(s, BTN)
        self.assertEqual(
            root.preordertraversal(),
            "42,-100,12,28,100,111")

if __name__ == '__main__':
    unittest.main()
