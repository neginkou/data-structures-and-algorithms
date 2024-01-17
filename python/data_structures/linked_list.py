class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_value):
        new_node = Node(new_value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if not self.head:
            return

        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        if not self.head:
            return

        current = self.head
        while current:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def delete(self, value):
        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

# Unit tests
if __name__ == "__main__":
    # Create a Linked List
    linked_list = LinkedList()

    # Test append
    linked_list.append(1)
    linked_list.append(3)
    linked_list.append(2)
    linked_list.append(5)
    print("Appended List:")
    # Expected output: 1 -> 3 -> 2 -> 5
    current = linked_list.head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("X")

    # Test insert_before
    linked_list.insert_before(3, 4)
    print("Insert Before:")
    # Expected output: 1 -> 4 -> 3 -> 2 -> 5
    current = linked_list.head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("X")

    # Test insert_after
    linked_list.insert_after(3, 6)
    print("Insert After:")
    # Expected output: 1 -> 4 -> 3 -> 6 -> 2 -> 5
    current = linked_list.head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("X")

    # Test delete
    linked_list.delete(6)
    print("Delete:")
    # Expected output: 1 -> 4 -> 3 -> 2 -> 5
    current = linked_list.head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("X")
