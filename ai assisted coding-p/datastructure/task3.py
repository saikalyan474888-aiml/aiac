class Node:
    """Represents a node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Implementation of a Singly Linked List."""

    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        """Display all elements of the linked list."""
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Example
linked_list = LinkedList()

linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)

print("Linked List:")
linked_list.display()