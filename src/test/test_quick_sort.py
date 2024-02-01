import unittest
from ..quick_sort import sort


class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        arr = [9, 3, 7, 4, 69, 420, 42]
        sort(arr);
        self.assertEqual(arr,[3, 4, 7, 9, 42, 69, 420])
