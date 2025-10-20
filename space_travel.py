route = input().split("||")
fuel = int(input())
ammunition = int(input())

for element in route:
    do = element.split()
    command = do[0]

    if command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break

    integer = int(do[1])

    if command == "Travel":
        if fuel >= integer:
            fuel -= integer
            print(f"The spaceship travelled {integer} light-years.")
        else:
            print("Mission failed.")
            break
    elif command == "Enemy":
        if ammunition >= integer:
            ammunition -= integer
            print(f"An enemy with {integer} armour is defeated.")
        elif fuel >= integer * 2:
            fuel -= integer * 2
            print(f"An enemy with {integer} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break

    elif command == "Repair":
        added_ammunition = 2 * integer
        ammunition += added_ammunition
        fuel += integer
        print(f"Ammunitions added: {added_ammunition}.")
        print(f"Fuel added: {integer}.")
