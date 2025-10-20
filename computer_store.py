total_price = 0
taxes = 0
total = 0

while True:
    command = input()

    if command == "special" or command == "regular":
        break

    if float(command) < 0:
        print("Invalid price!")
        continue

    total_price += float(command)

# compute taxes and totals
taxes = 0.20 * total_price
total = total_price + taxes

if total_price == 0:
    print("Invalid order!")
else:
    if command == "special":
        total *= 0.90  # 10% discount on the final price

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total:.2f}$")
