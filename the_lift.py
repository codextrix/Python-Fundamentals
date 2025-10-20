# mine
# people_waiting = int(input())
# current_state_of_the_lift = list(map(int, input().split()))
#
# for i in range(len(current_state_of_the_lift)):
#     free = 4 - current_state_of_the_lift[i]
#     if free > 0:
#         boarded = min(free, people_waiting)
#         current_state_of_the_lift[i] += boarded
#         people_waiting -= boarded
#         if people_waiting == 0:
#             break
#
# if people_waiting == 0 and any(w < 4 for w in current_state_of_the_lift):
#     print("The lift has empty spots!")
#     print(" ".join(map(str, current_state_of_the_lift)))
# elif people_waiting > 0:
#     print(f"There isn't enough space! {people_waiting} people in a queue!")
#     print(" ".join(map(str, current_state_of_the_lift)))
# else:
#     print(" ".join(map(str, current_state_of_the_lift)))

# Mario Zahariew:
tourists = int(input())
lift = [int(element) for element in input().split()]
capacity = 4

for i in range(len(lift)):
    free = capacity - lift[i]

    if free > 0 and tourists > 0:
        to_board = min(free, tourists)
        lift[i] += to_board
        tourists -= to_board

if tourists == 0 and any(element < capacity for element in lift):
    print("The lift has empty spots!")
    print(" ".join(map(str, lift)))
elif tourists > 0:
    print(f"There isn't enough space! {tourists} people in a queue!")
    print(" ".join(map(str, lift)))
else:
    print(" ".join(map(str, lift)))