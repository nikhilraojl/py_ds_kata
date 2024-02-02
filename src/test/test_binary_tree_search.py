import unittest

from ..proj_utils.binary_tree_node import BinaryNode
from ..binary_tree_search import breadth_first_search, depth_first_search

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

    def test_binary_tree_breadth_first_search(self):
        self.assertEqual(breadth_first_search(self.tree, 45), True)
        self.assertEqual(breadth_first_search(self.tree, 7), True)
        self.assertEqual(breadth_first_search(self.tree, 69), False)
    
    def test_binary_tree_depth_first_search(self):
        self.assertEqual(depth_first_search(self.tree, 45), True)
        self.assertEqual(depth_first_search(self.tree, 7), True)
        self.assertEqual(depth_first_search(self.tree, 69), False)
