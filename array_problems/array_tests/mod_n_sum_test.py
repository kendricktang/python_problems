import unittest
import numpy as np
from array_algs.mod_n_sum import mod_n_sum as mns

class TestModNSum(unittest.TestCase):
    """Test suite for mod_n_sum"""
        
    def test_single_case(self):
        """Test an array with a single value"""
        array = [42]
        np.testing.assert_array_equal(mns(array),[0])

    def test_zero_mod_n(self):
        """Test an array where sum(array[0:i]) is 0 mod n for some i"""
        array = [1, 3, 10, 2, 30, 104, 12, 43]
        np.testing.assert_array_equal(mns(array),[0, 1, 2, 3])

    def test_not_zero_mod_n(self):
        """Test an array where sum(array[0:i]) is not 0 mod n for all i"""
        array = [1, 3, 10, 3, 5, 104, 12, 42]
        np.testing.assert_array_equal(mns(array),[1, 2, 3])
        
        
if __name__ == '__main__':
    unittest.main()
