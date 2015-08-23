import unittest
from bintree_algs.binarytree2 import BinaryTreeNode2 as BTN
from bintree_algs.makebintree import makefromstring as mfs
from bintree_algs.makebintree import makefromtraversals as mft


class TestMakeFromPreorderTraversals(unittest.TestCase):
    """Test suite for makebintree.makefromtraversals() with preorder traversal
    as an input."""

    def test_singlecase(self):
        """Test a tree with just a root."""
        s = "42"
        root = mfs(s, BTN)
        inord = root.inordertraversal()
        preord = root.preordertraversal()
        postord = root.postordertraversal()
        root2 = mft(BTN, inord, preorder=preord)
        inord2 = root2.inordertraversal()
        preord2 = root2.preordertraversal()
        postord2 = root2.postordertraversal()

        self.assertEqual(inord, inord2)
        self.assertEqual(preord, preord2)
        self.assertEqual(postord, postord2)

    def test_rightonly(self):
        """Test a tree with only a right side."""
        s = "42[-100(12(10)[11(17)])[32]]"
        root = mfs(s, BTN)
        inord = root.inordertraversal()
        preord = root.preordertraversal()
        postord = root.postordertraversal()
        root2 = mft(BTN, inord, preorder=preord)
        inord2 = root2.inordertraversal()
        preord2 = root2.preordertraversal()
        postord2 = root2.postordertraversal()

        self.assertEqual(inord, inord2)
        self.assertEqual(preord, preord2)
        self.assertEqual(postord, postord2)

    def test_leftonly(self):
        """Test a tree with only a left side."""
        s = "42(-100(12(10)[11[17]])[23])"
        root = mfs(s, BTN)
        inord = root.inordertraversal()
        preord = root.preordertraversal()
        postord = root.postordertraversal()
        root2 = mft(BTN, inord, preorder=preord)
        inord2 = root2.inordertraversal()
        preord2 = root2.preordertraversal()
        postord2 = root2.postordertraversal()

        self.assertEqual(inord, inord2)
        self.assertEqual(preord, preord2)
        self.assertEqual(postord, postord2)

    def test_bothchildren(self):
        """Test a tree which has both children."""
        s = "42(-100(12)[28])[100[111]]"
        root = mfs(s, BTN)
        inord = root.inordertraversal()
        preord = root.preordertraversal()
        postord = root.postordertraversal()
        root2 = mft(BTN, inord, preorder=preord)
        inord2 = root2.inordertraversal()
        preord2 = root2.preordertraversal()
        postord2 = root2.postordertraversal()

        self.assertEqual(inord, inord2)
        self.assertEqual(preord, preord2)
        self.assertEqual(postord, postord2)


class TestMakeFromPostorderTraversals(unittest.TestCase):
    """Test suite for makebintree.makefromtraversals() with postorder traversal
    as an input."""

    def test_singlecase(self):
        """Test a tree with just a root."""
        s = "42"
        root = mfs(s, BTN)
        inord = root.inordertraversal()
        preord = root.preordertraversal()
        postord = root.postordertraversal()
        root2 = mft(BTN, inord, postorder=postord)
        inord2 = root2.inordertraversal()
        preord2 = root2.preordertraversal()
        postord2 = root2.postordertraversal()

        self.assertEqual(inord, inord2)
        self.assertEqual(preord, preord2)
        self.assertEqual(postord, postord2)

    def test_rightonly(self):
        """Test a tree with only a right side."""
        s = "42[-100(12(10)[11(17)])[32]]"
        root = mfs(s, BTN)
        inord = root.inordertraversal()
        preord = root.preordertraversal()
        postord = root.postordertraversal()
        root2 = mft(BTN, inord, postorder=postord)
        inord2 = root2.inordertraversal()
        preord2 = root2.preordertraversal()
        postord2 = root2.postordertraversal()

        self.assertEqual(inord, inord2)
        self.assertEqual(preord, preord2)
        self.assertEqual(postord, postord2)

    def test_leftonly(self):
        """Test a tree with only a left side."""
        s = "42(-100(12(10)[11[17]])[23])"
        root = mfs(s, BTN)
        inord = root.inordertraversal()
        preord = root.preordertraversal()
        postord = root.postordertraversal()
        root2 = mft(BTN, inord, postorder=postord)
        inord2 = root2.inordertraversal()
        preord2 = root2.preordertraversal()
        postord2 = root2.postordertraversal()

        self.assertEqual(inord, inord2)
        self.assertEqual(preord, preord2)
        self.assertEqual(postord, postord2)

    def test_bothchildren(self):
        """Test a tree which has both children."""
        s = "42(-100(12)[28])[100[111]]"
        root = mfs(s, BTN)
        inord = root.inordertraversal()
        preord = root.preordertraversal()
        postord = root.postordertraversal()
        root2 = mft(BTN, inord, postorder=postord)
        inord2 = root2.inordertraversal()
        preord2 = root2.preordertraversal()
        postord2 = root2.postordertraversal()

        self.assertEqual(inord, inord2)
        self.assertEqual(preord, preord2)
        self.assertEqual(postord, postord2)

if __name__ == '__main__':
    unittest.main()
