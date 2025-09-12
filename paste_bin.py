# 1

name = input()
if name == "Johnny":
    print("Hello, my love!")
else:
    print(f"Hello, {name}!")

# 2

ages = int(input())
drink = ""
if ages <= 14:
    drink = "toddy"
elif ages <= 18:
    drink = "coke"
elif ages <= 21:
    drink = "beer"
else:
    drink = "whisky"
print(f"drink {drink}")

# 3

number_of_messages = int(input())
for message in range(number_of_messages):
    current_number = int(input())
    current_message = ""
    if current_number == 88:
        current_message = "Hello"
    elif current_number == 86:
        current_message = "How are you?"
    elif current_number < 88:
        current_message = "GREAT!"
    elif current_number > 88:  # else
        current_message = "Bye."
    print(current_message)

# 4

divisor = int(input())
boundary = int(input())
for current_number in range(boundary, divisor - 1, -1):
    if current_number % divisor == 0:
        break
print(current_number)

# 5
number_of_orders = int(input())
total_price = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        # if price_per_capsule not in range(0.01, 100.01):
        continue
    elif days < 1 or days > 31:
        # if days not in range(1, 32):
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    price = price_per_capsule * days * capsules_per_day
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")

# 6

number_of_strings = int(input())
for current_strings in range(number_of_strings):
    current_string = input()
    if "," in current_string or \
            "." in current_string or \
            "_" in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")

# 10

first_string = input()
second_string = input()
for character_index in range(len(first_string)):
    left_part = second_string[: character_index + 1]
    right_part = first_string[character_index + 1:]
    new_string = left_part + right_part
    if first_string[character_index] != second_string[character_index]:
        print(new_string)

# my_string = "alabalaportokala"
# print(my_string)
# # [start:end:step]
# print(my_string[1:5:2])
# # [start:end]
# print(my_string[1:5])
# # [:end]
# print(my_string[:5])
# # [start:]
# print(my_string[5:])


# 12

quantity_of_decorations = int(input())
remaining_days = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
total_cost = 0
total_spirit = 0
for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        total_cost += ornament_set_price * quantity_of_decorations
        total_spirit += 5
    if current_day % 3 == 0:
        total_cost += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
        total_spirit += 3 + 10
    if current_day % 5 == 0:
        total_cost += tree_lights_price * quantity_of_decorations
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price
if remaining_days % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")

# https: // peps.python.org / pep - 000
# 8 /
# https: // peps.python.org / pep - 0020 / https: // peps.python.org / pep - 0020 /