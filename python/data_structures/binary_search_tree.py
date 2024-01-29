from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.root = None

    def add(self, value):
        # method body here
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        def walk(verify_node, node_being_added):

            if node_being_added.value < verify_node.value:
                if verify_node.left is None:
                    verify_node.left = node_being_added
                else:
                    walk(verify_node.left, node_being_added)
            elif node_being_added.value > verify_node.value:
                if verify_node.right is None:
                    verify_node.right = node_being_added
                else:
                    walk(verify_node.right, node_being_added)
        walk(self.root, new_node)

    def contains(self, value_to_find):

        if self.root is None:
            return

        def walk(node):

            if node is None:
                return False

            if value_to_find == node.value:
                return True
            elif value_to_find > node.value:
                return walk(node.right)
            elif value_to_find < node.value:
                return walk(node.left)

        return walk(self.root)
