numbers = input().split(", ")
count_of_beggars = int(input())
brings_home = []

for coin in numbers:
    brings_home.append(int(coin))

start_index = 0
sum_of_coins = []
for beggar in range(count_of_beggars):
    current = 0

    for index in range(start_index, len(brings_home), count_of_beggars):
        current += brings_home[index]

    sum_of_coins.append(current)
    start_index += 1

print(sum_of_coins)