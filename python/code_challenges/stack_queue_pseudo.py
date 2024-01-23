from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()  # For enqueue operations
        self.stack2 = Stack()  # For dequeue operations

    def enqueue(self, value):
        # To enqueue, simply push the value onto stack1
        self.stack1.push(value)

    def dequeue(self):
        if self.stack2.is_empty():
            if self.stack1.is_empty():
                return None  # PseudoQueue is empty
            else:
                # Transfer elements from stack1 to stack2 to reverse the order
                while not self.stack1.is_empty():
                    self.stack2.push(self.stack1.pop())

        # Pop the top element from stack2 (which represents the front of the queue)
        return self.stack2.pop()
