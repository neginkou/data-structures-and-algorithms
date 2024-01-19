class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:


    def __init__(self):
        self.head = None

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def __str__(self):
        current = self.head
        string_representation = ""

        while current:
            formatted_current_value = f"{{ {current.value} }} -> "
            string_representation += formatted_current_value
            current = current.next

        string_representation += "NULL"

        return string_representation

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, target, value):
        if self.head is None:
            raise TargetError("List is empty")
        if self.head.value == target:
            self.insert(value)
            return
        current = self.head
        while current.next and current.next.value != target:
            current = current.next
        if current.next is None:
            raise TargetError(f"Target {target} not found in the list")
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def insert_after(self, target, value):
        current = self.head
        while current and current.value != target:
            current = current.next
        if current is None:
            raise TargetError(f"Target {target} not found in the list")
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def kthFromEnd(self, k):
        if not isinstance(k, int) or k < 0:
            raise ValueError("k must be a non-negative integer")

        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next

        if k >= length:
            raise TargetError("k is out of range")

        current = self.head
        for _ in range(length - k - 1):
            current = current.next

        return current.value



class TargetError(Exception):
    pass


