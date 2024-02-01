from ..linear_search import search
from unittest import TestCase


class TestLinearSearch(TestCase):
    def test_linear(self):
        arr: list[int] = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
        self.assertTrue(search(arr, 69))
        self.assertTrue(search(arr, 90))
        self.assertTrue(search(arr, 90))
        self.assertTrue(search(arr, 1337))
        self.assertTrue(search(arr, 69420))
        self.assertFalse(search(arr, 100))
        self.assertFalse(search(arr, 500))
        self.assertFalse(search(arr, 0))
