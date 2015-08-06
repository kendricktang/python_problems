import unittest
import numpy as np
from stack_algs.binarysearchtree import BinarySearchTree as BST


class TestBinarySearch(unittest.TestCase):
    """Test suite for BinarySearchTree"""

    def test_single_case(self):
        """Test an array with a single value"""
        bst = BST(1)
        self.assertTrue(is_sorted(BST.print_BST_test(bst.top)))

    def test_descending_case(self):
        """Test an array with a descending values"""
        array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        bst = BST.fromarray(array)
        self.assertTrue(is_sorted(BST.print_BST_test(bst.top)))

    def test_ascending_case(self):
        """Test an array with ascending values"""
        array = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        bst = BST.fromarray(array)
        self.assertTrue(is_sorted(BST.print_BST_test(bst.top)))

    def test_pop(self):
        """Test a randomized array"""
        array = np.random.randint(-100, 100, 100)
        bst = BST.fromarray(array)
        self.assertTrue(is_sorted(BST.print_BST_test(bst.top)))


def is_sorted(array):
    """Checks to see if an array is sorted"""
    if len(array) <= 1:
        return True
    return any(array[i] <= array[i+1] for i in xrange(len(array)-1))


if __name__ == '__main__':
    unittest.main()
