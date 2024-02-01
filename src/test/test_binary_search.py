from ..binary_search import search
import unittest


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        arr = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420];
        self.assertTrue(search(arr, 69))
        self.assertFalse(search(arr, 1336))
        self.assertTrue(search(arr, 69420))
        self.assertFalse(search(arr, 69421))
        self.assertTrue(search(arr, 1))
        self.assertFalse(search(arr, 0))
