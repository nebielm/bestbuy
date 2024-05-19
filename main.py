import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quant=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quant=500),
                products.Product("Google Pixel 7", price=500, quant=250)
                ]
best_buy = store.Store(product_list)


def start():
    while True:
        print("   Store Menu\n   ----------")
        menu = ["List all products in store", "Show total amount in store",
                "Make an order", "Quit"]
        for i, option in enumerate(menu):
            print(str(i+1) + ". " + option)
        return int(input("Please choose a number: "))


def list_products(store_obj):
    products_in_store = store_obj.get_all_products()
    for i, product in enumerate(products_in_store):
        print(str(i+1) + ". " + product.show())


def show_total_amount(store_obj):
    print(f"Total of {store_obj.get_total_quantity()} items in store")


def make_order(store_obj):
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
            print(e)
            print("Error adding product!")
    print(f"Order made! Total payment:{total_payment}")


def main():
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
