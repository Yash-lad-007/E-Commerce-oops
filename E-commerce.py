import random

# --- Product Class ---
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price})"

# --- Customer Class ---
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def __str__(self):
        return f"Customer: {self.name}"

# --- Cart Class ---
class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        self.items.append((product, quantity))

    def total_price(self):
        return sum(product.price * quantity for product, quantity in self.items)

    def show_cart(self):
        print("\nCart Summary:")
        for product, quantity in self.items:
            print(f"- {product.name} x{quantity} = ${product.price * quantity}")
        print(f"Total: ${self.total_price():.2f}\n")

# --- Order Class ---
class Order:
    def __init__(self, customer, cart):
        self.order_id = random.randint(1000, 9999)
        self.customer = customer
        self.cart = cart

    def summary(self):
        print("===== ORDER SUMMARY =====")
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer.name}")
        self.cart.show_cart()
        print("=========================")

# --- Main Logic ---
if __name__ == "__main__":
    # Create Products
    p1 = Product(1, "Laptop", 1000)
    p2 = Product(2, "Mouse", 25)
    p3 = Product(3, "Keyboard", 45)

    # Create a Customer
    customer = Customer(101, "Alice")

    # Create a Cart and add Products
    cart = Cart()
    cart.add_product(p1, 1)
    cart.add_product(p2, 2)
    cart.add_product(p3, 1)

    # Create and display Order
    order = Order(customer, cart)
    order.summary()
