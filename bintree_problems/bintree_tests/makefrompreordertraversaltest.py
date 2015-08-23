import unittest
from bintree_algs.binarytree2 import BinaryTreeNode2 as BTN
from bintree_algs.makefrompreordertraversal import makebintree as mbt
from bintree_algs.makebintree import makefromstring as mfs


class TestMakeFromPreorderTraversals(unittest.TestCase):
    """Test suite for makefrompreordertraversal.makebintree()."""

    def test_singlecase(self):
        """Test a tree with just a root."""
        array = [42, None, None]
        s = "42"
        root = mbt(array)
        root_ = mfs(s, BTN)
        self.assertEqual(
            root.preordertraversal(),
            root_.preordertraversal())
        self.assertEqual(
            root.preordertraversal(),
            root_.preordertraversal())
        self.assertEqual(
            root.postordertraversal(),
            root_.postordertraversal())

    def test_rightonly(self):
        """Test a tree with only a right side."""
        array = [
            42, None, -100, 12, 10, None, None, 11, 17, None, None, None,
            32, None, None]
        s = "42[-100(12(10)[11(17)])[32]]"
        root = mbt(array)
        root_ = mfs(s, BTN)
        self.assertEqual(
            root.preordertraversal(),
            root_.preordertraversal())
        self.assertEqual(
            root.preordertraversal(),
            root_.preordertraversal())
        self.assertEqual(
            root.postordertraversal(),
            root_.postordertraversal())

    def test_leftonly(self):
        """Test a tree with only a left side."""
        array = [
            42, -100, 12, 10, None, None, 11, None, 17, None, None, 23,
            None, None, None]
        s = "42(-100(12(10)[11[17]])[23])"
        root = mbt(array)
        root_ = mfs(s, BTN)
        self.assertEqual(
            root.preordertraversal(),
            root_.preordertraversal())
        self.assertEqual(
            root.preordertraversal(),
            root_.preordertraversal())
        self.assertEqual(
            root.postordertraversal(),
            root_.postordertraversal())

    def test_bothchildren(self):
        """Test a tree which has both children."""
        array = [
            42, -100, 12, None, None, 28, None, None, 100, None, 111, None,
            None]
        s = "42(-100(12)[28])[100[111]]"
        root = mbt(array)
        root_ = mfs(s, BTN)
        self.assertEqual(
            root.preordertraversal(),
            root_.preordertraversal())
        self.assertEqual(
            root.preordertraversal(),
            root_.preordertraversal())
        self.assertEqual(
            root.postordertraversal(),
            root_.postordertraversal())


if __name__ == '__main__':
    unittest.main()
