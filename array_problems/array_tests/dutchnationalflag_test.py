import unittest
from array_algs.dutchnationalflag import dutchnationalflag as dnf

class TestDutchNationalFlag(unittest.TestCase):
    """Test suite for dutchnationalflag"""

    def test_singlecase(self):
        """Test an array with a single value"""
        array = [100]
        pivotindex = 0
        pivot = array[pivotindex]
        dnf(array, pivotindex)
        self.assertTrue(is_sorted(map(lambda x: cmp(x, pivot), array)))

    def test_allgreater(self):
        """Test an array where all values are greater than pivot"""
        array = [1, 3, 10, 2, 0]
        pivotindex = 4
        pivot = array[pivotindex]
        dnf(array, pivotindex)
        self.assertTrue(is_sorted(map(lambda x: cmp(x, pivot), array)))

    def test_allless(self):
        """Test an array where all values are less than pivot"""
        array = [-3, -10, -5, -2, 0]
        pivotindex = 4
        pivot = array[pivotindex]
        dnf(array, pivotindex)
        self.assertTrue(is_sorted(map(lambda x: cmp(x, pivot), array)))

    def test_allequal(self):
        """Test an array of all the same value"""
        array = [42, 42, 42, 42, 42, 42]
        pivotindex = 4
        pivot = array[pivotindex]
        dnf(array, pivotindex)
        self.assertTrue(is_sorted(map(lambda x: cmp(x, pivot), array)))

    def test_multiplepivots(self):
        """Test an array where the pivot occurs multiple times"""
        array = [12, 30, 32, 14, 10, 28, 32, 34, 41, 50, 32]
        pivotindex = 6
        pivot = array[pivotindex]
        dnf(array, pivotindex)
        self.assertTrue(is_sorted(map(lambda x: cmp(x, pivot), array)))

def is_sorted(array):
    """Checks to see if an array is sorted"""
    if len(array) == 1:
        return True
    return any(x <= y for (x, y) in zip(array, array[1:]))

if __name__ == '__main__':
    unittest.main()
