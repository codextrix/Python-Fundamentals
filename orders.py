products = {}

while True:
    command = input()
    if command == "buy":
        break

    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = {"price": price, "qty": 0}

    products[name]["price"] = price
    products[name]["qty"] += quantity

for name, data in products.items():
    total = data["price"] * data["qty"]
    print(f"{name} -> {total:.2f}")
