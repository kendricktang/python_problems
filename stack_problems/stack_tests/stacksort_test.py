import unittest
from stackqueue_algs.stack import Stack as S


class StackSortTest(unittest.TestCase):
    """Test suite for Stack sort"""

    def test_single_case(self):
        """Test a stack with a single value"""
        array = [-42]
        s = S.fromarray(array)
        s.sort()
        sortedarray = s.toarray()
        self.assertTrue(issorted(sortedarray))

    def test_empty_case(self):
        """Test an empty stack"""
        s = S()
        s.sort()
        sortedarray = s.toarray()
        self.assertTrue(issorted(sortedarray))

    def test_random_case(self):
        """Test a random stack """
        array = [
            -42, 102, 49, 32, -120, 84, 23, 455, 88, -199,
            -20, -199, 42, 41, 12, 28]
        s = S.fromarray(array)
        s.sort()
        sortedarray = s.toarray()
        self.assertTrue(issorted(sortedarray))


def issorted(array):
    """Checks to see if an array is sorted"""
    if len(array) <= 1:
        return True
    return any(array[i] <= array[i+1] for i in xrange(len(array)-1))


if __name__ == '__main__':
    unittest.main()
