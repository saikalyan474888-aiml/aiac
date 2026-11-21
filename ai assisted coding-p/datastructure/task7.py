class CafeteriaQueue:
    """Queue for serving students in the order they arrive."""

    def __init__(self):
        self.orders = []

    def add_order(self, student, food):
        """Add a student's order to the queue."""
        self.orders.append((student, food))

    def serve_order(self):
        """Serve the first order in the queue."""
        if not self.orders:
            return "No orders waiting"

        return self.orders.pop(0)

    def display_orders(self):
        """Display all waiting orders."""
        if not self.orders:
            print("No orders waiting")
            return

        print("Waiting Orders:")

        for student, food in self.orders:
            print(student, "-", food)


# Example
cafeteria = CafeteriaQueue()

cafeteria.add_order("Anirudh", "Burger")
cafeteria.add_order("Rahul", "Pizza")
cafeteria.add_order("Sai", "Sandwich")

cafeteria.display_orders()

print("Serving:", cafeteria.serve_order())

cafeteria.display_orders()