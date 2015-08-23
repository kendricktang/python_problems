import unittest
from numpy import random as rand
from search_algs.arraysearch import findindexequalsvalue as fiev


class TestFindFirstOccurrence(unittest.TestCase):
    """A test suite for findfirstoccurrence(). Input is sorted,
    and elements are distinct."""

    def test_bigtest(self):
        rand.seed(1)
        testsize = 50
        incount = 0
        outcount = 0
        for ind in xrange(testsize):
            size = rand.randint(100)
            array = rand.randint(-10, 50, size).tolist()
            array = list(set(array))
            array.sort()
            val = fiev(array)
            if val == -1:
                for i in xrange(len(array)):
                    self.assertNotEqual(i, array[i])
            else:
                incount += 1
                self.assertEqual(val, array[val])
        print incount, outcount

"""
    def test_trivialcase_pass(self):
        array = [0]
        self.assertEqual(0, fiev(array))

    def test_trivialcase_fail(self):
        pass
        array = [42]
        self.assertEqual(-1, fiev(array))

    def test_textbookcase_pass(self):
        array = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        self.assertEqual(2, fiev(array))

    def test_textbookcase_fail(self):
        array = [-14, -10, 3, 108, 108, 243, 285, 285, 285, 401]
        self.assertEqual(-1, fiev(array))
"""

if __name__ == "__main__":
    unittest.main()
