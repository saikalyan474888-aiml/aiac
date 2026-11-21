class Inventory:
    # Use a dictionary to store each item and its quantity
    def __init__(self):
        self.items = {}

    # Add a new item or increase quantity if it already exists
    def add_item(self, name, quantity):
        if name not in self.items:
            self.items[name] = 0
        self.items[name] += quantity

    # Remove quantity from an item, but never let stock go below 0
    def remove_item(self, name, quantity):
        if name not in self.items:
            return

        if quantity >= self.items[name]:
            self.items[name] = 0
        else:
            self.items[name] -= quantity

    # Return the current stock for an item, or 0 if it does not exist
    def get_stock(self, name):
        if name not in self.items:
            return 0
        return self.items[name]


# Tests for Inventory.
inv = Inventory()

inv.add_item("Pen", 10)
assert inv.get_stock("Pen") == 10

inv.remove_item("Pen", 5)
assert inv.get_stock("Pen") == 5

inv.add_item("Book", 3)
assert inv.get_stock("Book") == 3

# Extra tests
inv.add_item("Pen", 7)
assert inv.get_stock("Pen") == 12

assert inv.get_stock("Notebook") == 0

inv.remove_item("Pen", 100)
assert inv.get_stock("Pen") == 0


# This message prints only if all tests pass.
print("All Task 4 tests passed!")