collection_of_items = input().split("|")
budget = float(input())
selling_price_list = []
total_shopping_sum = 0
total_selling_sum = 0
ticket_price = 150

for item in collection_of_items:
    current_item = item.split("->")
    item_type, item_value = current_item[0], float(current_item[1])

    if budget < item_value:
        continue
    if (item_type != "Clothes" and item_value > 50.00) and\
        (item_type != "Shoes" and item_value > 35.00) and\
            (item_type != "Accessories" and item_value > 20.50):
        continue
    else:
        budget -= item_value
        total_shopping_sum += item_value
        selling_price = item_value + 0.4 * item_value
        total_selling_sum += selling_price
        selling_price_list.append(f"{selling_price:.2f}")


print(" ".join(selling_price_list))
profit = total_selling_sum - total_shopping_sum
budget += total_selling_sum
print(f"Profit: {profit:.2f}")

if budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")