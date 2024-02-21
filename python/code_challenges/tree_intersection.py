from data_structures.binary_tree import BinaryTree

def tree_intersection(tree_a, tree_b):
    """
    Find the intersection between two binary trees.
    """
    if not tree_a.root or not tree_b.root:
        return []

    def traverse(tree):
        """
        Traverse the binary tree and return a set of values.
        """
        values = set()
        def _traverse(node):
            if node:
                values.add(node.value)
                _traverse(node.left)
                _traverse(node.right)
        _traverse(tree.root)
        return values

    values_a = traverse(tree_a)
    values_b = traverse(tree_b)

    return list(values_a.intersection(values_b))
