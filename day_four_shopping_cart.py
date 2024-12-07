class ShoppingCart:
    """
    A class representing a shopping cart.
    """

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.cart = []  # List to store items in the cart

    def add_item(self, item_name: str, price: float, quantity: int) -> None:
        """
        Add or update an item in the shopping cart.

        :param item_name: Name of the item
        :param price: Price of the item  (positive float)
        :param quantity: Quantity of the item  (positive int)
        """

        if not self._is_valid_item(item_name, price, quantity):
            return

        # Check if the item already exists in the cart and update it
        for item in self.cart:
            if item["item_name"] == item_name:
                item["quantity"] += quantity
                print(f"Updated {item_name} quantity to {item['quantity']}.")
                return

        # Add new item to the cart
        self.cart.append({"item_name": item_name,
                          "price": price,
                          "quantity": quantity
                          }
                         )

        print(f"Added {quantity} x {item_name} @${price:.2f} each to the cart")

    def remove_item(self, item_name: str) -> None:
        """
        Remove an item from the shopping cart by name.

        :param item_name: Name of the item to be removed
        """
        for item in self.cart:
            if (item["item_name"]) == item_name:
                self.cart.remove(item)
                print(f"Removed {item_name} from the cart")
                return
            print(f"{item_name} not found in the cart")

    def view_cart(self) -> None:
        """Display the items in the shopping cart."""

        if not self.cart:
            print("your cart is empty.")
            return

        print("Items in your cart:")

        for idx, item in enumerate(self.cart, start=1):
            print(
                f"{idx} : {item['item_name']} x {item['quantity']} @ ${item['price']:.2f} ")

    def calculate_total(self) -> float:
        """Calculate and return the total cost of items in the shopping cart."""

        total = sum([item["price"] * item["quantity"] for item in self.cart])
        print(f"Total cost is : ${total:.2f}")
        return total

    @staticmethod
    def _is_valid_item(item_name: str, price: float, quantity: int) -> bool:
        """
        Validate the item details.

        :param item_name: Name of the item
        :param price: Price of the item
        :param quantity: Quantity of the item
        :return: True if valid, False otherwise
        """

        if not isinstance(item_name, str) or not item_name.strip():
            print("Item name must be a non-empty string.")
            return False

        if not isinstance(price, (int, float)) or price <= 0:
            print("Price must be a positive number.")
            return False

        if not isinstance(quantity, (int)) or quantity <= 0:
            print("Qty must be a positive number.")
            return False

        return True


cart = ShoppingCart()
cart.add_item("Apple", 0.99, 5)
cart.add_item("Milk", 2.49, 2)
cart.view_cart()
cart.calculate_total()
cart.remove_item("Apple")
cart.view_cart()
cart.calculate_total()
cart.add_item(123, 2.49, 2)
