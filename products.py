class Product:
    """Represents a specific type of product available in the store.
     It encapsulates information about the product, including its name and price.
     Additionally, it includes an attribute to keep track of the total quantity
     of items of that product currently available in the store."""
    def __init__(self, name, price, quant):
        """Sets instance variables, which it gets from user."""
        if len(str(name)) <= 0:
            raise Exception("You have to enter a name.")
        self.name = str(name)
        if float(price) <= 0.0:
            raise Exception("The price has to be a positive number.")
        self.price = float(price)
        if int(quant) <= 0:
            raise Exception("The quantity has to be a positive number.")
        self.quant = int(quant)
        self.active = True

    def get_quantity(self):
        """Getter function for quantity. Returns the quantity (float)."""
        return self.quant

    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0,
        deactivates the product."""
        self.quant -= quantity
        if self.quant <= 0:
            self.active = False

    def is_active(self):
        """Getter function for active.
        Returns True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Returns a string that represents the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quant}"

    def buy(self, quantity):
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem, raises an Exception."""
        if quantity > self.quant:
            raise Exception("Order quantity not in storage.")
        total_price = self.price * quantity
        self.quant -= quantity
        if self.quant == 0:
            self.active = False
        return float(total_price)


class NoneStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 1)
        self.quant = 0

    def set_quantity(self, quantity):
        return 0

    def show(self):
        """Returns a string that represents the product."""
        return f"{self.name}, Price: {self.price}"

    def buy(self, quantity):
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase."""
        total_price = self.price * quantity
        return float(total_price)


class LimitedProduct(Product):
    def __init__(self, name, price, quant, maximum_order):
        super().__init__(name, price, quant)
        self.maximum = maximum_order

    def show(self):
        """Returns a string that represents the product."""
        return f"{self.name}, Price: {self.price}, Maximum Order: {self.maximum}"

    def buy(self, quantity):
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of ordering mor than max.-order, raises an Exception."""
        if quantity > self.maximum:
            raise Exception(f"Product can be purchased only {self.maximum} times per order.")
        total_price = self.price * quantity
        self.quant -= quantity
        if self.quant == 0:
            self.active = False
        return float(total_price)
