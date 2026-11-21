class Queue:
    """Implementation of a FIFO Queue using Python list."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item."""
        if self.size() == 0:
            return "Queue is empty"
        return self.items.pop(0)

    def peek(self):
        """Return the front item without removing it."""
        if self.size() == 0:
            return "Queue is empty"
        return self.items[0]

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)


# Example
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front:", queue.peek())
print("Dequeued:", queue.dequeue())
print("Front after dequeue:", queue.peek())
print("Queue size:", queue.size())