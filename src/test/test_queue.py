import unittest
from ..queue import Queue

class TestQueue(unittest.TestCase):
    def test_queue(self):
        list = Queue();

        list.enqueue(5);
        list.enqueue(7);
        list.enqueue(9);

        self.assertEqual(list.deque(), 5)
        self.assertEqual(list.length, 2)

        list.enqueue(11);
        self.assertEqual(list.deque(), 7)
        self.assertEqual(list.deque(), 9)
        self.assertEqual(list.peek(), 11)
        self.assertEqual(list.deque(), 11)
        self.assertEqual(list.deque(), None)
        self.assertEqual(list.length, 0)

        list.enqueue(69);
        self.assertEqual(list.peek(), 69)
        self.assertEqual(list.length, 1)
