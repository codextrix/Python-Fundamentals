rooms = int(input())
total_free_chairs = 0
message_to_output = []
for room in range(rooms):
    command = input().split()
    chairs = command[0]
    people = int(command[1])
    chair_difference = len(chairs) - people

    if chair_difference < 0:
        message_to_output.append(f"{abs(chair_difference)} more chairs needed in room {room + 1}")
    else:
        total_free_chairs += chair_difference

if message_to_output:
    for message in message_to_output:
        print(message)
else:
     print(f"Game On, {total_free_chairs} free chairs left")
       