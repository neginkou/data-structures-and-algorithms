from data_structures.invalid_operation_error import InvalidOperationError

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.front = None
        self.back = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.back is None:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):

        if self.front is None:
           raise InvalidOperationError("Method not allowed on empty collection")


        dequeue_value = self.front.value

        self.front = self.front.next

        if self.front is None:
            self.back = None

        return dequeue_value

    def peek(self):

        if self.back is None:
         raise InvalidOperationError("Method not allowed on empty collection")

        peeked_value = self.front.value

        return peeked_value

    def is_empty(self):
        if self.back is None:
            return True
