import unittest
from ..singly_linked_list import SinglyLinkedList
from ..doubly_linked_list import DoublyLinkedList


class TestLinkedList(unittest.TestCase):
    def helper(self, l_list: SinglyLinkedList | DoublyLinkedList):
        l_list.append(5)
        l_list.append(7)
        l_list.append(9)

        self.assertEqual(l_list.get(2), 9)
        self.assertEqual(l_list.removeAt(1), 7)
        self.assertEqual(l_list.length, 2)

        l_list.append(11)
        self.assertEqual(l_list.removeAt(1), 9)
        self.assertEqual(l_list.remove(9), None)
        self.assertEqual(l_list.removeAt(0), 5)
        self.assertEqual(l_list.removeAt(0), 11)
        self.assertEqual(l_list.length, 0)

        l_list.prepend(5)
        l_list.prepend(7)
        l_list.prepend(9)

        self.assertEqual(l_list.get(2), 5)
        self.assertEqual(l_list.get(0), 9)
        self.assertEqual(l_list.remove(9), 9)
        self.assertEqual(l_list.length, 2)
        self.assertEqual(l_list.get(0), 7)

    def test_singly_linked_list(self):
        s_list = SinglyLinkedList()
        self.helper(s_list)
    
    def test_doubly_linked_list(self):
        d_list = DoublyLinkedList()
        self.helper(d_list)
