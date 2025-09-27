cards = input().split()
count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):
    middle = len(cards) // 2
    left_part = cards[:middle]
    right_part = cards[middle:]
    shuffled_deck = []

    for card_index in range(len(left_part)):
        shuffled_deck.append(left_part[card_index])
        shuffled_deck.append(right_part[card_index])

    cards = shuffled_deck.copy()

print(cards)