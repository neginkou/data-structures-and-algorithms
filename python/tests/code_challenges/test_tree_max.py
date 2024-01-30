import pytest
from data_structures.binary_tree import BinaryTree, Node


def test_max_val():
    tree = BinaryTree(Node(10))
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected

def test_max_val_empty_tree():
    tree = BinaryTree()

    actual = tree.find_maximum_value()
    expected = None

    assert actual == expected
