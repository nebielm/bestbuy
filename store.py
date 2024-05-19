class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        if product in self.product_list:
            raise Exception("Product already in store.")
        self.product_list.append(product)

    def remove_product(self, product):
        if product not in self.product_list:
            raise Exception("Product not in store.")
        self.product_list.remove(product)

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        active_products = []
        for product in self.product_list:
            if product.active:
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        total_price = 0
        for item in shopping_list:
            product = item[0]
            quantity = item[1]
            total_price += product.buy(quantity)
        return total_price
