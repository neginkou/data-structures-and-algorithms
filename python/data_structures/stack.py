from data_structures.invalid_operation_error import InvalidOperationError

class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """
    Creates a stack data structure, with push, pop, is_empty and peek methods
    """

    def __init__(self):
        # initialization here
        self.top = None

    def push(self, value):
        new_node = Node(value)


        # Why do you have to point the new node to the current top? why can't you just assign self.top to new_node?
        new_node.next = self.top

        self.top = new_node

    def pop(self):

        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")

        popped_value = self.top.value

        self.top = self.top.next

        return popped_value

    def is_empty(self):
        if self.top is None:
            return True

    def peek(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        peeked_value = self.top.value

        return peeked_value
    