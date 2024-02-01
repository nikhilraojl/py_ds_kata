import unittest
from ..stack import Stack

class TestStack(unittest.TestCase):
    def test_stack(self):
        list = Stack();

        list.push(5);
        list.push(7);
        list.push(9);

        self.assertEqual(list.pop(), 9)
        self.assertEqual(list.length, 2)

        list.push(11);
        self.assertEqual(list.pop(), 11)
        self.assertEqual(list.pop(), 7)
        self.assertEqual(list.peek(), 5)
        self.assertEqual(list.pop(), 5)
        self.assertEqual(list.pop(), None)

        list.push(69);
        self.assertEqual(list.peek(), 69)
        self.assertEqual(list.length, 1)
