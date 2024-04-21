# Name: Oluwadeyi Ayobami
# File Name: test.py
# Description: File used to run tests on written code to check for any possible errors

import unittest
from fractions import Fraction

from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """Tests the sum of the data is the expected value"""
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """Test that it can sum fractions properly"""
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()