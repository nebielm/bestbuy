class Store:
    """Class will hold and manage products, and will allow the user to make
     a purchase of multiple products at once."""
    def __init__(self, product_list):
        """Gets list of product from user."""
        self.product_list = product_list

    def add_product(self, product):
        """Adds product to store."""
        if product in self.product_list:
            raise Exception("Product already in store.")
        self.product_list.append(product)

    def remove_product(self, product):
        """Removes a product from store."""
        if product not in self.product_list:
            raise Exception("Product not in store.")
        self.product_list.remove(product)

    def get_total_quantity(self):
        """Returns how many items are in the store in total."""
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """Returns all products in the store that are active."""
        active_products = []
        for product in self.product_list:
            if product.active:
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order."""
        total_price = 0
        for item in shopping_list:
            product = item[0]
            quantity = item[1]
            total_price += product.buy(quantity)
        return total_price
