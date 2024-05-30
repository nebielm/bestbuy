import products
import store
import promotions


def start():
    """Prints main menu and returns user choice."""
    while True:
        print("   Store Menu\n   ----------")
        menu = ["List all products in store", "Show total amount in store",
                "Make an order", "Quit"]
        for i, option in enumerate(menu):
            print(str(i+1) + ". " + option)
        try:
            return int(input("Please choose a number: "))
        except Exception as e:
            print(f"Your input was invalid. {e}")


def list_products(store_obj):
    """Prints all available products in store."""
    products_in_store = store_obj.get_all_products()
    for i, product in enumerate(products_in_store):
        print(str(i+1) + ". " + product.show())


def show_total_amount(store_obj):
    """Print total amount of products in store."""
    print(f"Total of {store_obj.get_total_quantity()} items in store")


def make_order(store_obj):
    """allows user to make an order by asking which product and how much he/she
    wants to purchase. Updates store after purchase and prints total amount of
    purchase."""
    products_in_store = store_obj.get_all_products()
    for i, product in enumerate(products_in_store):
        print(str(i+1) + ". " + product.show())
    total_payment = 0
    while True:
        order_choice = input("When you want to finish order, enter empty text.\n"
                             "Which product # do you want? ")
        amount = input("What amount do you want? ")
        if len(order_choice) == 0 and len(amount) == 0:
            break
        try:
            total_payment += store_obj.order([(products_in_store[int(order_choice) - 1], int(amount))])
            print("Product added to list!")
        except Exception as e:
            print(f"Error adding product!: {e}")
    print(f"Order made! Total payment:{total_payment}")


def main():
    """Creates instances of Products, adds them to the store and
    create a user interface, through using the functions, defined in this file.
    Adds the functionality that user can end the program from running."""
    product_list = [products.Product("MacBook Air M2", price=1450, quant=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quant=500),
                    products.Product("Google Pixel 7", price=500, quant=250),
                    products.NoneStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quant=250, maximum_order=1)
                    ]
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)
    best_buy = store.Store(product_list)
    while True:
        menu_choice = start()
        if menu_choice == 1:
            list_products(best_buy)
        elif menu_choice == 2:
            show_total_amount(best_buy)
        elif menu_choice == 3:
            make_order(best_buy)
        elif menu_choice == 4:
            break
        else:
            continue


if __name__ == "__main__":
    main()
