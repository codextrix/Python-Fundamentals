# 1

numbers = input().split()
opposite_numbers = []
for element in numbers:
    opposite_number = -int(element)
    opposite_numbers.append(opposite_number)
print(opposite_numbers)

# 2

factor = int(input())
count = int(input())
numbers = []
for multiplier in range(1, count + 1):
    numbers.append(factor * multiplier)
print(numbers)

# 3

team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
game_was_terminated = False
players = input().split()
for player in players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminated = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_was_terminated:  # if game_was_terminated == True
    print("Game was terminated")

# 4
money_as_string = input().split(", ")
number_of_beggars = int(input())
money_as_integers = []
for money in money_as_string:
    money_as_integers.append(int(money))
beggars_sums = []
start_index = 0
for current_beggar in range(number_of_beggars):
    current_beggar_sum = 0
    for index in range(start_index, len(money_as_integers), number_of_beggars):
        current_beggar_sum += money_as_integers[index]
    beggars_sums.append(current_beggar_sum)
    start_index += 1
print(beggars_sums)

# 5
deck_of_cards = input().split()
number_of_shuffles = int(input())
for current_shuffle in range(number_of_shuffles):
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]
    deck_after_shuffling = []
    for card_index in range(len(left_part)):  # for card_index in range(len(right_part)):
        deck_after_shuffling.append(left_part[card_index])
        deck_after_shuffling.append(right_part[card_index])
    deck_of_cards = deck_after_shuffling.copy()
print(deck_of_cards)

# 9

collection_of_items = input().split("|")
budget = float(input())
ticket_price = 150
selling_price_list = []
total_shopping_sum = 0
total_selling_sum = 0
for item in collection_of_items:
    new_item = item.split("->")
    current_item, current_price = new_item[0], float(new_item[1])
    if budget < current_price:
        continue
    if current_item == "Clothes" and current_price <= 50.00:
        budget -= current_price
        total_shopping_sum += current_price
        selling_price = current_price + current_price * 0.4
        total_selling_sum += selling_price
        selling_price_list.append(f"{selling_price:.2f}")
    elif current_item == "Shoes" and current_price <= 35.00:
        budget -= current_price
        total_shopping_sum += current_price
        selling_price = current_price + current_price * 0.4
        total_selling_sum += selling_price
        selling_price_list.append(f"{selling_price:.2f}")
    elif current_item == "Accessories" and current_price <= 20.50:
        budget -= current_price
        total_shopping_sum += current_price
        selling_price = current_price + current_price * 0.4
        total_selling_sum += selling_price
        selling_price_list.append(f"{selling_price:.2f}")
print(" ".join(selling_price_list))
profit = total_selling_sum - total_shopping_sum
print(f"Profit: {profit:.2f}")
budget += total_selling_sum
if budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")

# 10


events = input().split("|")
total_energy = 100
total_coins = 100
bakery_is_open = True
for event in events:
    event_values = event.split("-")
    event_type, event_value = event_values[0], int(event_values[1])
    if event_type == "rest":
        initial_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif event_type == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {event_type}.")
        else:
            bakery_is_open = False
            break
if bakery_is_open:  # if bakery_is_open == True
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
else:
    print(f"Closed! Cannot afford {event_type}.")

# my_list = [1, 2, 3, 4, 5]
# my_list = [1, "a", 3, "a", 5.14, "a", 5]
# my_list = ["c", "a", "C"]

# print(my_list)
# my_list.sort(reverse=False)
# print(my_list)
#
# print(my_list)
# my_list.pop()
# print(my_list)
# print(my_list)
# number = my_list.pop()
# print(number)

# index = -20
# element = "test"
# my_list.insert(index, element)
# print(my_list)
#
# if True in my_list:
#     number = my_list.index(True)
#     print(number)
#
# repetition = my_list.count(5)
# print(repetition)

# my_list.reverse()
# print(my_list)
# my_list = my_list[::-1]
# print(my_list)

# index = 20
# del my_list[index]
# print(my_list)
#
# some_element = "a"
# while some_element in my_list:
#     my_list.remove(some_element)
#     print(my_list)
# # for index in range(len(my_list)):
#     if my_list[index] == "a":
#         del my_list[index]
#
# print(my_list)