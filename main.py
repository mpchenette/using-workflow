class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} (${self.price}) - {self.stock} in stock"

class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.id in self.items:
            self.items[product.id]['quantity'] += quantity
        else:
            self.items[product.id] = {'product': product, 'quantity': quantity}

    def remove_product(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def get_total(self):
        total = 0
        for item in self.items.values():
            total += item['product'].price * item['quantity']
        return total

    def __str__(self):
        cart_contents = [f"{item['product'].name} x {item['quantity']}" for item in self.items.values()]
        return "Cart: " + ", ".join(cart_contents)

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.cart = Cart()

    def __str__(self):
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
