from data_structures.binary_tree import BinaryTree
from collections import deque


def breadth_first(tree):
    if not tree.root:
        return []

    result = []
    queue = deque()
    queue.append(tree.root)

    while queue:
        current_node = queue.popleft()
        result.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result
    
