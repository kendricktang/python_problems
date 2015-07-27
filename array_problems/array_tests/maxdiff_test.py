import unittest
from array_algs.maxdiff import maxdiff, maxdiff_2, maxdiff_k

class TestMaxDiff(unittest.TestCase):
    """Test suite for maxdiff method"""
    def test_empty(self):
        lst = []
        self.assertEqual(maxdiff(lst), 0)

    def test_samevals(self):
        lst = [42, 42, 42, 42, 42]
        self.assertEqual(maxdiff(lst), 0)

    def test_descending(self):
        lst = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
        self.assertEqual(maxdiff(lst), 0)

    def test_ascending(self):
        lst = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.assertEqual(maxdiff(lst), 10)

    def test_random(self):
        lst = [-10, -3, -6, 3, 3, -10, 5, 7, 6, 6, -4, -7, -8, -8, -9, 0, 8, 1, 7]
        self.assertEqual(maxdiff(lst), 18)

class TestMaxDiff_2(unittest.TestCase):
    """Test suite for maxdiff_2 method"""
    def test_empty(self):
        lst = []
        self.assertEqual(maxdiff_2(lst), 0)

    def test_samevals(self):
        lst = [42, 42, 42, 42, 42]
        self.assertEqual(maxdiff_2(lst), 0)

    def test_descending(self):
        lst = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
        self.assertEqual(maxdiff_2(lst), 0)

    def test_ascending(self):
        lst = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.assertEqual(maxdiff_2(lst), 10)

    def test_random(self):
        lst = [-10, -3, -6, 3, 3, -10, 5, 7, 6, 6, -4, -7, -8, -8, -9, 0, 8, 1, 7]
        self.assertEqual(maxdiff_2(lst), 34)

if __name__ == '__main__':
    unittest.main()

