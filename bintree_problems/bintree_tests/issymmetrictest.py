import unittest
from bintree_algs.binarytree import BinaryTreeNode as BTN
from bintree_algs.makebintree import makebintree as mbt


class TestIsSymmetric(unittest.TestCase):
    """Test suite for BinaryTreeNode.issymmetric()."""

    def test_singlecase(self):
        """Test a tree with just a root."""
        s = "42"
        root = mbt(s, BTN)
        self.assertTrue(root.issymmetric())

    def test_symmetric(self):
        """Test a tree which is symmetric."""
        s = "42(10(1)[2(3)[4]])[10(2(4)[3])[1]]"
        root = mbt(s, BTN)
        self.assertTrue(root.issymmetric())

    def test_unsymmetric(self):
        """Test a tree which is unsymmetric."""
        s = "42(10(1)[2(3)[4[5]]])[10(2(4)[3])[1]]"
        root = mbt(s, BTN)
        self.assertFalse(root.issymmetric())


if __name__ == '__main__':
    unittest.main()
