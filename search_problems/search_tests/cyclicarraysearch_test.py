import unittest
from numpy import random as rand
from search_algs.cyclicarraysearch import findstartcyclic as fsc


class TestFindStartCyclic(unittest.TestCase):
    """A test suite for findstartcyclic(), where the input is a cyclically
    sorted array of distinct elements."""

    def test_singleelement(self):
        array = [42]
        self.assertEqual(fsc(array), 0)

    def test_regularlysorted(self):
        array = [-100, -50, -25, -1, 0, 16, 32, 64]
        self.assertEqual(fsc(array), 0)

    def test_rotatedleftbyone(self):
        array = [-50, -25, -1, 0, 16, 32, 64, -100]
        self.assertEqual(fsc(array), 7)

    def test_rotatedrightbyone(self):
        array = [64, -100, -50, -25, -1, 0, 16, 32]
        self.assertEqual(fsc(array), 1)

    def test_bigtest(self):
        rand.seed(1)
        testsize = 10
        for ind in xrange(testsize):
            # Create a randomized cyclically sorted array with distinct
            # elements.
            size = rand.randint(1, 200)
            _array = rand.randint(-100, 100, size).tolist()
            _array = list(set(_array))  # Got rid of duplicates.
            _array.sort()
            rotation = rand.randint(0, len(_array))

            array = _array[rotation:] + _array[:rotation]
            if rotation:
                self.assertEqual(len(array) - rotation, fsc(array))
            else:
                self.assertEqual(0, fsc(array))


if __name__ == "__main__":
    unittest.main()
