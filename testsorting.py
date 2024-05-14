"""
This module contains tests for the sorting algorithms learnt in the A-Level CS course
"""

import unittest
from sorting import Sort

class TestSorting(Sort, unittest.TestCase):
    """
    This class contains unit tests for the sorting algorithms
    """

    def test_bubble_sort(self):
        """
        This function tests the bubble sort algorithm
        """

        arr = [5, 2, 8, 1, 9]
        result = self.bubble_sort(arr)
        expected = [1, 2, 5, 8, 9]
        self.assertEqual(result, expected)

    def test_insertion_sort(self):
        """
        This function tests the insertion sort algorithm
        """

        arr = [5, 2, 8, 1, 9]
        result = self.insertion_sort(arr)
        expected = [1, 2, 5, 8, 9]
        self.assertEqual(result, expected)

    def test_merge_sort(self):
        """
        This function tests the merge sort algorithm
        """

        arr = [5, 2, 8, 1, 9]
        result = self.merge_sort(arr)
        expected = [1, 2, 5, 8, 9]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
