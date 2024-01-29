class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.root = None

    def pre_order(self):
        # method body here
        """
        expected = ["a", "b", "d", "e", "c", "f", "g"]
        """

        def walk(node):

            if node is None:
                return []

            result = [node.value]
            left_result = walk(node.left)
            right_result = walk(node.right)

            return result + left_result + right_result




        return walk(self.root)

    def in_order(self):
        """
        expected = ["d", "b", "e", "a", "f", "c", "g"]
                    left          main     right
        """

        def walk(node):
            if node is None:
                return []

            result = [node.value]
            left_result = walk(node.left)
            right_result = walk(node.right)

            return left_result + result + right_result

        return walk(self.root)

    def post_order(self):
        """
        expected = ["d", "e", "b", "f", "g", "c", "a"]
                    left           right          main
        """

        def walk(node):
            if node is None:
                return []
            result = [node.value]
            left_result = walk(node.left)
            right_result = walk(node.right)

            return left_result + right_result + result

        return walk(self.root)

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
