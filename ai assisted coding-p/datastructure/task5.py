import heapq


class PriorityQueue:
    """Priority Queue implementation using heapq."""

    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        """Add an item with a given priority."""
        heapq.heappush(self.queue, (-priority, item))

    def dequeue(self):
        """Remove and return the highest-priority item."""
        if not self.queue:
            return "Priority Queue is empty"

        priority, item = heapq.heappop(self.queue)
        return item

    def display(self):
        """Display all items in the priority queue."""
        if not self.queue:
            print("Priority Queue is empty")
            return

        print("Priority Queue:")

        for priority, item in sorted(self.queue):
            print("Item:", item, "Priority:", -priority)


# Example
pq = PriorityQueue()

pq.enqueue("Student A", 2)
pq.enqueue("Student B", 5)
pq.enqueue("Student C", 1)

pq.display()

print("Removed:", pq.dequeue())