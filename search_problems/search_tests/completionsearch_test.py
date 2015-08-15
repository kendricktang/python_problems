import unittest
from numpy import random as rand
from search_algs.completionsearch import completionsearch as cs


class TestCompletionSearch(unittest.TestCase):
    """A test suite for completionsearch(). Input arrays contain nonnegative
    values, and the newsum must be less than the current sum."""

    def test_singleelement(self):
        array = [4200]
        delta = 1e-5
        newsum = 42
        upperbound = cs(array, newsum)
        self.assertAlmostEqual(
            newsum, sum([min(x, upperbound) for x in array]), delta=delta)

    def test_textbook(self):
        array = [90, 30, 100, 40, 20]
        delta = 1e-5
        newsum = 210
        upperbound = cs(array, newsum)
        self.assertAlmostEqual(
            newsum, sum([min(x, upperbound) for x in array]), delta=delta)

    def test_bigtest(self):
        rand.seed(1)
        testsize = 10
        delta = 1e-5
        for ind in xrange(testsize):
            size = rand.randint(1, 2000)
            array = rand.randint(0, 100, size)
            sumofarray = sum(array)
            newsum = rand.randint(0, sumofarray)
            upperbound = cs(array, newsum)
            self.assertAlmostEqual(
                newsum, sum([min(x, upperbound) for x in array]), delta=delta)


if __name__ == "__main__":
    unittest.main()
