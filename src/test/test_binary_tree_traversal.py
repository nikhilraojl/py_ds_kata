import unittest

from ..proj_utils.binary_tree_node import BinaryNode
from ..binary_tree_traversal import pre_order_traversal, in_order_traversal, post_order_traversal

tree_structure = {
    "value": 20,
    "right": {
        "value": 50,
        "right": {
            "value": 100,
            "right": None,
            "left": None,
        },
        "left": {
            "value": 30,
            "right": {
                "value": 45,
                "right": None,
                "left": None,
            },
            "left": {
                "value": 29,
                "right": None,
                "left": None,
            }
        },
    },
    "left": {
        "value": 10,
        "right": {
            "value": 15,
            "right": None,
            "left": None,
        },
        "left": {
            "value": 5,
            "right": {
                "value": 7,
                "right": None,
                "left": None,
            },
            "left": None,
        }
    }
}

def create_tree[T](value: T, left, right) -> BinaryNode[T] | None:
    if not left:
        left = None
    else:
        left = create_tree(left["value"], left["left"], left["right"])

    if not right:
        right = None
    else:
        right = create_tree(right["value"], right["left"], right["right"])

    return BinaryNode(value, left, right)

class TestBinaryTreeTraversal(unittest.TestCase):
    tree: BinaryNode[int]

    def setUp(self) -> None:
        tree = create_tree(**tree_structure)
        if tree:
            self.tree = tree
        else:
            self.tree= BinaryNode(0, None, None)

    def test_binary_tree_pre_order_traversal(self):
        self.assertEqual(pre_order_traversal(self.tree), [ 20, 10, 5, 7, 15, 50, 30, 29, 45, 100])
    
    def test_binary_tree_in_order_traversal(self):
        self.assertEqual(in_order_traversal(self.tree), [ 5, 7, 10, 15, 20, 29, 30, 45, 50, 100])
     
    def test_binary_tree_post_order_traversal(self):
        self.assertEqual(post_order_traversal(self.tree), [ 7, 5, 15, 10, 29, 45, 30, 100, 50, 20])
    
    def test_binary_tree_breadth_first_traversal(self):
        self.assertEqual(post_order_traversal(self.tree), [ 20, 10, 50, 5, 15, 30, 100, 7, 29, 45])
