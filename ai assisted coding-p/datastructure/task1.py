class Stack:
    """Implementation of a Stack using Python list."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        """Check whether the stack is empty."""
        return len(self.items) == 0


# Example
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top:", stack.peek())
print("Popped:", stack.pop())
print("Top after pop:", stack.peek())
print("Is empty:", stack.is_empty())