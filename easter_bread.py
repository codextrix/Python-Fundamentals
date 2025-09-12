budget = float(input())
flour_price = float(input())

eggs_price = 0.75 * flour_price
milk_price_per_liter = 1.25 * flour_price
milk_per_loave = milk_price_per_liter / 4

loave_price = eggs_price + flour_price + milk_per_loave

money_left = budget

loaves = 0
colored_eggs = 0

while money_left >= loave_price:
    loaves += 1
    money_left -= loave_price
    colored_eggs += 3

    if loaves % 3 == 0:
        colored_eggs -= loaves - 2

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")