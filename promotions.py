class Promotion:
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        discount_price = product.price / 2
        return (quantity // 2) * discount_price


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        return (quantity // 3) * product.price


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        return (product.price * quantity) * (self.percent / 100)
