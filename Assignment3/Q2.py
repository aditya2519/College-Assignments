# Class representing a product in the online store
class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock_quantity})"


# Class representing an item in the shopping cart
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def total_price(self):
        return self.product.price * self.quantity


# Class representing the shopping cart
class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product, quantity):
        if product.stock_quantity >= quantity:
            item = CartItem(product, quantity)
            self.cart_items.append(item)
            product.stock_quantity -= quantity  # Reduce stock in the product
            print(f"Added {quantity} of {product.name} to the cart.")
        else:
            print(f"Insufficient stock for {product.name}. Available: {product.stock_quantity}")

    def remove_product(self, product_name):
        for item in self.cart_items:
            if item.product.name == product_name:
                item.product.stock_quantity += item.quantity  # Restore stock
                self.cart_items.remove(item)
                print(f"Removed {product_name} from the cart.")
                return
        print(f"{product_name} not found in the cart.")

    def view_cart(self):
        if not self.cart_items:
            print("Your cart is empty.")
            return
        total = 0
        print("Items in your cart:")
        for item in self.cart_items:
            print(f"- {item.product.name}: {item.quantity} @ ${item.product.price:.2f} each")
            total += item.total_price()
        print(f"Total price: ${total:.2f}")

    def checkout(self):
        if not self.cart_items:
            print("Your cart is empty. Cannot checkout.")
            return
        total = sum(item.total_price() for item in self.cart_items)
        print(f"Total amount to pay: ${total:.2f}. Thank you for your purchase!")
        self.cart_items.clear()  # Clear the cart after checkout


# Class representing a user
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = ShoppingCart()

# Example usage of the system:
# Creating products
product1 = Product("Laptop", 999.99, 10)
product2 = Product("Smartphone", 499.99, 5)
product3 = Product("Headphones", 199.99, 20)

# Creating a user
user = User("Aditya Survase", "password123")

# Adding products to the cart
user.cart.add_product(product1, 1)
user.cart.add_product(product2, 2)
user.cart.add_product(product3, 1)

# Viewing the cart
user.cart.view_cart()

# Removing a product
user.cart.remove_product("Smartphone")

# Viewing the cart after removal
user.cart.view_cart()

# Checking out
user.cart.checkout()

# Attempt to view cart after checkout
user.cart.view_cart()
