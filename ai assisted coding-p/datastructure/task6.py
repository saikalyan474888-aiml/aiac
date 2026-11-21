from collections import deque


class DequeDS:
    """Implementation of a Double-Ended Queue."""

    def __init__(self):
        self.items = deque()

    def insert_front(self, item):
        """Insert an item at the front."""
        self.items.appendleft(item)

    def insert_rear(self, item):
        """Insert an item at the rear."""
        self.items.append(item)

    def remove_front(self):
        """Remove and return the front item."""
        if not self.items:
            return "Deque is empty"

        return self.items.popleft()

    def remove_rear(self):
        """Remove and return the rear item."""
        if not self.items:
            return "Deque is empty"

        return self.items.pop()

    def display(self):
        """Display all elements."""
        print("Deque:", list(self.items))


# Example
dq = DequeDS()

dq.insert_front(10)
dq.insert_rear(20)
dq.insert_front(5)

dq.display()

print("Removed from front:", dq.remove_front())
print("Removed from rear:", dq.remove_rear())

dq.display()