class ProductNode:
    """Represents a product in the BST."""

    def __init__(self, product_id, product_name):
        self.product_id = product_id
        self.product_name = product_name
        self.left = None
        self.right = None


class ProductSearch:
    """Binary Search Tree for fast product ID searching."""

    def __init__(self):
        self.root = None

    def insert(self, root, product_id, product_name):
        """Insert a product into the BST."""

        if root is None:
            return ProductNode(product_id, product_name)

        if product_id < root.product_id:
            root.left = self.insert(
                root.left,
                product_id,
                product_name
            )

        elif product_id > root.product_id:
            root.right = self.insert(
                root.right,
                product_id,
                product_name
            )

        return root

    def search(self, root, product_id):
        """Search for a product using its product ID."""

        if root is None:
            return None

        if product_id == root.product_id:
            return root

        if product_id < root.product_id:
            return self.search(root.left, product_id)

        return self.search(root.right, product_id)


# Example
products = ProductSearch()

products.root = products.insert(products.root, 101, "Laptop")
products.root = products.insert(products.root, 105, "Smartphone")
products.root = products.insert(products.root, 103, "Headphones")
products.root = products.insert(products.root, 110, "Smart Watch")

product_id = 103

result = products.search(products.root, product_id)

if result:
    print("Product Found")
    print("Product ID:", result.product_id)
    print("Product Name:", result.product_name)
else:
    print("Product not found")