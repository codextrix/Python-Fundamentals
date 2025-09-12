n = int(input())

total = 0

for i in range(n):
    price = float(input())
    days = int(input())
    capsules = int(input())

    # Validation
    if price < 0.01 or price > 100.00:
        continue
    if days < 1 or days > 31:
        continue
    if capsules < 1 or capsules > 2000:
        continue

    coffee = price * days * capsules
    total += coffee
    print(f"The price for the coffee is: ${coffee:.2f}")

print(f"Total: ${total:.2f}")
