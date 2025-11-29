stock = {}
sold = 0

command = input()

while command != "Complete":
    parts = command.split()
    action = parts[0]
    quantity = int(parts[1])
    food = parts[2]

    if action == "Receive":
        if quantity > 0:
            if food in stock:
                stock[food] += quantity
            else:
                stock[food] = quantity

    elif action == "Sell":
        if food not in stock:
            print(f"You do not have any {food}.")
        else:
            if stock[food] < quantity:
                sold_quantity = stock[food]
                sold += sold_quantity
                print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
                del stock[food]
            else:
                stock[food] -= quantity
                sold += quantity
                print(f"You sold {quantity} {food}.")
                if stock[food] == 0:
                    del stock[food]

    command = input()

for food_name, qty in stock.items():
    print(f"{food_name}: {qty}")

print(f"All sold: {sold} goods")
