import products

bose = products.Product("Bose QuietComfort Earbuds", price=250, quant=500)
mac = products.Product("MacBook Air M2", price=1450, quant=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

print(bose.show())
print(mac.show())

print(bose.set_quantity(1000))
print(bose.show())
