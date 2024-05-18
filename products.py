class Product:
    def __init__(self, name, price, quant):
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
        return self.quant

    def set_quantity(self, quantity):
        self.quant -= quantity
        if self.quant <= 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quant}"

    def buy(self, quantity):
        if quantity > self.quant:
            raise Exception("Order quantity not in storage.")
        total_price = self.price * quantity
        self.quant -= quantity
        if self.quant == 0:
            self.active = False
        return float(total_price)
