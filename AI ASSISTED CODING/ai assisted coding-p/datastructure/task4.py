class Node:
    """Represents a node in a Binary Search Tree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    """Implementation of a Binary Search Tree."""

    def __init__(self):
        self.root = None

    def insert(self, root, data):
        """Recursively insert a value into the BST."""

        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    def inorder(self, root):
        """Perform in-order traversal of the BST."""

        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


# Example
bst = BST()

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    bst.root = bst.insert(bst.root, value)

print("In-order Traversal:")
bst.inorder(bst.root)