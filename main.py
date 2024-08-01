class Product:
    """
    A class to represent a product.

    Attributes:
        id (int): The unique identifier for the product.
        name (str): The name of the product.
        price (float): The price of the product.
        stock (int): The number of items in stock.
    """

    def __init__(self, id, name, price, stock):
        """
        Initialize a new product.

        Args:
            id (int): The unique identifier for the product.
            name (str): The name of the product.
            price (float): The price of the product.
            stock (int): The number of items in stock.
        """
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        """
        Return a string representation of the product.

        Returns:
            str: A string describing the product.
        """
        return f"{self.name} (${self.price}) - {self.stock} in stock"


class Cart:
    """
    A class to represent a shopping cart.

    Attributes:
        items (dict): A dictionary to store cart items with product ID as key.
    """

    def __init__(self):
        """
        Initialize a new shopping cart.
        """
        self.items = {}

    def add_product(self, product, quantity):
        """
        Add a product to the cart.

        Args:
            product (Product): The product to add.
            quantity (int): The quantity of the product to add.
        """
        if product.id in self.items:
            self.items[product.id]['quantity'] += quantity
        else:
            self.items[product.id] = {'product': product, 'quantity': quantity}

    def remove_product(self, product_id):
        """
        Remove a product from the cart by its ID.

        Args:
            product_id (int): The ID of the product to remove.
        """
        if product_id in self.items:
            del self.items[product_id]

    def get_total(self):
        """
        Calculate the total price of all items in the cart.

        Returns:
            float: The total price of the cart.
        """
        total = 0
        for item in self.items.values():
            total += item['product'].price * item['quantity']
        return total

    def __str__(self):
        """
        Return a string representation of the cart contents.

        Returns:
            str: A string describing the cart contents.
        """
        cart_contents = [f"{item['product'].name} x {item['quantity']}" for item in self.items.values()]
        return "Cart: " + ", ".join(cart_contents)


class User:
    """
    A class to represent a user.

    Attributes:
        username (str): The username of the user.
        email (str): The email address of the user.
        cart (Cart): The shopping cart associated with the user.
    """

    def __init__(self, username, email):
        """
        Initialize a new user.

        Args:
            username (str): The username of the user.
            email (str): The email address of the user.
        """
        self.username = username
        self.email = email
        self.cart = Cart()

    def __str__(self):
        """
        Return a string representation of the user.

        Returns:
            str: A string describing the user.
        """
        return f"User: {self.username}, Email: {self.email}"


# Example usage
if __name__ == "__main__":
    # Create some products
    product1 = Product(1, "Laptop", 999.99, 10)
    product2 = Product(2, "Smartphone", 499.99, 20)

    # Create a user
    user = User("john_doe", "john@example.com")

    # Add products to the user's cart
    user.cart.add_product(product1, 1)
    user.cart.add_product(product2, 2)

    # Print user details and cart contents
    print(user)
    print(user.cart)
    print(f"Total: ${user.cart.get_total():.2f}")
