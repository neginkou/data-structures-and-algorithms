class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def find_maximum_value(self):
        def find_max_recursive(node):
            if node is None:
                return float('-inf')  # Return negative infinity for empty nodes
            max_left = find_max_recursive(node.left)
            max_right = find_max_recursive(node.right)
            return max(node.value, max_left, max_right)

        if self.root is None:
            return None  # Return None for an empty tree
        return find_max_recursive(self.root)

    def pre_order(self):
        def walk(node):
            if node is None:
                return []

            result = [node.value]
            left_result = walk(node.left)
            right_result = walk(node.right)

            return result + left_result + right_result

        return walk(self.root)

    def in_order(self):
        def walk(node):
            if node is None:
                return []

            result = [node.value]
            left_result = walk(node.left)
            right_result = walk(node.right)

            return left_result + result + right_result

        return walk(self.root)

    def post_order(self):
        def walk(node):
            if node is None:
                return []

            result = [node.value]
            left_result = walk(node.left)
            right_result = walk(node.right)

            return left_result + right_result + result

        return walk(self.root)
