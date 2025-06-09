# Test for 2d_prefix_sum.py
from array_string.prefix_sum.prefix_sum_2d import (
    construct_2d_prefix_sum,
    query_2d_prefix_sum,
)
import unittest


class Test2DPrefixSum(unittest.TestCase):
    def setUp(self):
        # Example matrix for testing
        self.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.prefix_sum = construct_2d_prefix_sum(self.matrix)

    def test_full_matrix(self):
        # Sum of all elements: 1+2+3+4+5+6+7+8+9 = 45
        result = query_2d_prefix_sum(self.prefix_sum, 0, 0, 2, 2)
        self.assertEqual(result, 45)

    def test_single_element(self):
        # Just the element at (1,1): 5
        result = query_2d_prefix_sum(self.prefix_sum, 1, 1, 1, 1)
        self.assertEqual(result, 5)

    def test_first_row(self):
        # First row: 1+2+3 = 6
        result = query_2d_prefix_sum(self.prefix_sum, 0, 0, 0, 2)
        self.assertEqual(result, 6)

    def test_first_column(self):
        # First column: 1+4+7 = 12
        result = query_2d_prefix_sum(self.prefix_sum, 0, 0, 2, 0)
        self.assertEqual(result, 12)

    def test_submatrix(self):
        # Middle 2x2 block: 5+6+8+9 = 28
        result = query_2d_prefix_sum(self.prefix_sum, 1, 1, 2, 2)
        self.assertEqual(result, 28)

    def test_top_left_2x2(self):
        # Top-left 2x2: 1+2+4+5 = 12
        result = query_2d_prefix_sum(self.prefix_sum, 0, 0, 1, 1)
        self.assertEqual(result, 12)

    def test_bottom_right_2x2(self):
        # Bottom-right 2x2: 5+6+8+9 = 28
        result = query_2d_prefix_sum(self.prefix_sum, 1, 1, 2, 2)
        self.assertEqual(result, 28)

    def test_entire_last_row(self):
        # Last row: 7+8+9 = 24
        result = query_2d_prefix_sum(self.prefix_sum, 2, 0, 2, 2)
        self.assertEqual(result, 24)


if __name__ == "__main__":
    unittest.main()
