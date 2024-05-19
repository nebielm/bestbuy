import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quant=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quant=500),
                products.Product("Google Pixel 7", price=500, quant=250)
                ]
best_buy = store.Store(product_list)


def start(store_obj):
    print("   Store Menu\n   ----------")
    menu = ["List all products in store", "Show total amount in store",
            "Make an order", "Quit"]
    for i, option in enumerate(menu):
        print(str(i+1) + ". " + option)


start(best_buy)
