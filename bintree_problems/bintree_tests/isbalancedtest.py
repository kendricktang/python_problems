import unittest
from bintree_algs.binarytree import BinaryTreeNode as BTN
from bintree_algs.makebintree import makebintree as mbt


class TestIsBalanced(unittest.TestCase):
    """Test suite for BinaryTreeNode.isbalanced()."""

    def test_singlecase(self):
        """Test a tree with just a root."""
        s = "42"
        root = mbt(s, BTN)
        self.assertTrue(root.isbalanced())

    def test_rightonly(self):
            """Test a tree with only a right side."""
            s = "42[-100(12(10)[11(17)])[32]]"
            root = mbt(s, BTN)
            self.assertFalse(root.isbalanced())

    def test_leftonly(self):
        """Test a tree with only a left side."""
        s = "42(-100(12(10)[11[17]])[23])"
        root = mbt(s, BTN)
        self.assertFalse(root.isbalanced())

    def test_bothchildren(self):
        """Test a tree which has both children."""
        s = "42(-100(12)[28])[100[111]]"
        root = mbt(s, BTN)
        self.assertTrue(root.isbalanced())


if __name__ == '__main__':
    unittest.main()
