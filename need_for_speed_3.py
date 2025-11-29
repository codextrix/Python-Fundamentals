n = int(input())
cars = {}

for _ in range(n):
    car_info = input().split("|")
    car, mileage, fuel = car_info[0], int(car_info[1]), int(car_info[2])
    cars[car] = {"mileage": mileage, "fuel": fuel}

while True:
    line = input()
    if line == "Stop":
        break

    command = line.split(" : ")
    action = command[0]

    if action == "Drive":
        car_name = command[1]
        distance = int(command[2])
        needed_fuel = int(command[3])

        if cars[car_name]["fuel"] < needed_fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car_name]["fuel"] -= needed_fuel
            cars[car_name]["mileage"] += distance
            print(f"{car_name} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")

            if cars[car_name]["mileage"] >= 100000:
                del cars[car_name]
                print(f"Time to sell the {car_name}!")

    elif action == "Refuel":
        car_name = command[1]
        fuel_needed = int(command[2])

        current_fuel = cars[car_name]["fuel"]
        space_left = 75 - current_fuel
        fuel_added = min(space_left, fuel_needed)

        cars[car_name]["fuel"] += fuel_added
        print(f"{car_name} refueled with {fuel_added} liters")

    elif action == "Revert":
        car_name = command[1]
        kilometers = int(command[2])

        new_mileage = cars[car_name]["mileage"] - kilometers
        if new_mileage < 10000:
            cars[car_name]["mileage"] = 10000
        else:
            cars[car_name]["mileage"] = new_mileage
            print(f"{car_name} mileage decreased by {kilometers} kilometers")

for car, info in cars.items():
    print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")
