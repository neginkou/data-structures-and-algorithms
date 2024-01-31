from data_structures.kary_tree import KaryTree, Node

def fizz_buzz_tree(original_tree):
    if original_tree is None:
        return None

    def fizz_buzz(node):
        if node.value % 3 == 0 and node.value % 5 == 0:
            return "FizzBuzz"
        elif node.value % 3 == 0:
            return "Fizz"
        elif node.value % 5 == 0:
            return "Buzz"
        else:
            return str(node.value)

    def clone_tree(original_node):
        if original_node is None:
            return None

        new_node = Node(fizz_buzz(original_node))
        new_node.children = [clone_tree(child) for child in original_node.children]

        return new_node

    new_root = clone_tree(original_tree.root)
    new_tree = KaryTree(new_root)

    return new_tree
