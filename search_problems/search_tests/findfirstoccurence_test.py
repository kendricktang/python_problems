import unittest
from numpy import random as rand
from search_algs.arraysearch import findfirstoccurrence as ffo


class TestFindFirstOccurrence(unittest.TestCase):
    """A test suite for findfirstoccurrence(). Input is sorted."""

    def test_trivialcase_pass(self):
        array = [42]
        k = 42
        self.assertEqual(0, ffo(array, k))

    def test_trivialcase_fail(self):
        array = [42]
        k = -42
        self.assertEqual(-1, ffo(array, k))

    def test_textbookcase_pass(self):
        array = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        self.assertEqual(3, ffo(array, 108))
        self.assertEqual(6, ffo(array, 285))

    def test_textbookcase_fail(self):
        array = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        self.assertEqual(-1, ffo(array, 0))
        self.assertEqual(-1, ffo(array, 100))

    def test_bigtest(self):
        """This only checks if (-1, -1) is not returned..."""
        rand.seed(1)
        testsize = 200
        for ind in xrange(testsize):
            size = rand.randint(1, 1500)
            array = rand.randint(-500, 500, size).tolist()
            array.sort()
            k = rand.randint(-500, 500)
            if k in array:
                self.assertEqual(array.index(k), ffo(array, k))
            else:
                self.assertEqual(-1, ffo(array, k))


if __name__ == "__main__":
    unittest.main()
