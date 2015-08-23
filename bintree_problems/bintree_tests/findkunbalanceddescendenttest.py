import unittest
from bintree_algs.binarytree import BinaryTreeNode as BTN
from bintree_algs.makebintree import makefromstring as mfs


class TestFindKUnbalancedDescendent(unittest.TestCase):
    """Test suite for BinaryTreeNode.findkunbalanceddescendent."""

    def test_singlecase(self):
        """Test a tree with just a root."""
        s = "42"
        root = mfs(s, BTN)
        self.assertIsNone(root.findkunbalanceddescendent(1))

    def test_rightonly(self):
        """Test a tree with only a right side."""
        s = "42[-100(12(10)[11(999)(17)])[32]]"
        root = mfs(s, BTN)
        self.assertEqual(
            root.findkunbalanceddescendent(1).val,
            12)
        self.assertEqual(
            root.findkunbalanceddescendent(2).val,
            -100)
        self.assertEqual(
            root.findkunbalanceddescendent(3).val,
            -100)

    def test_leftonly(self):
        """Test a tree with only a left side."""
        s = "42(-100(12(10)[11[17[112233]]])[23])"
        root = mfs(s, BTN)
        self.assertEqual(
            root.findkunbalanceddescendent(1).val,
            11)
        self.assertEqual(
            root.findkunbalanceddescendent(2).val,
            -100)
        self.assertEqual(
            root.findkunbalanceddescendent(3).val,
            -100)
        self.assertEqual(
            root.findkunbalanceddescendent(4).val,
            42)

    def test_strictrightonly(self):
        """Test a tree with only right children."""
        s = "1[2[3[4[5[6]]]]]"
        root = mfs(s, BTN)
        self.assertEqual(
            root.findkunbalanceddescendent(1).val,
            4)
        self.assertEqual(
            root.findkunbalanceddescendent(2).val,
            3)
        self.assertEqual(
            root.findkunbalanceddescendent(3).val,
            2)
        self.assertEqual(
            root.findkunbalanceddescendent(4).val,
            1)

    def test_strictleftonly(self):
        """Test a tree with only left children."""
        s = "1(2(3(4(5(6)))))"
        root = mfs(s, BTN)
        self.assertEqual(
            root.findkunbalanceddescendent(1).val,
            4)
        self.assertEqual(
            root.findkunbalanceddescendent(2).val,
            3)
        self.assertEqual(
            root.findkunbalanceddescendent(3).val,
            2)
        self.assertEqual(
            root.findkunbalanceddescendent(4).val,
            1)

    def test_bothchildren(self):
        """Test a tree which has both children."""
        s = "42(-100(12)[28])[100(2000(1)[2])[111]]"
        root = mfs(s, BTN)
        self.assertEqual(
            root.findkunbalanceddescendent(1).val,
            100)
        self.assertIsNone(root.findkunbalanceddescendent(2))


if __name__ == '__main__':
    unittest.main()
