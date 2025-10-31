number_commands = int(input())
parking = {}
for command in range(number_commands):
    current_command = input().split()
    action = current_command[0]
    if action == "register":
        username, plate = current_command[1], current_command[2]
        if username in parking.keys():
            print(f"ERROR: already registered with plate number {plate}")
        else:
            parking[username] = plate
            print(f"{username} registered {plate} successfully")
    elif action == "unregister":
        username = current_command[1]
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

for username, plate in parking.items():
    print(f"{username} => {plate}")
