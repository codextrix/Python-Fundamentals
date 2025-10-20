first_employee = int(input())
second_employee = int(input())
third_employee = int(input())

num_students = int(input())
time_needed = 0

total_capacity_per_hour = first_employee + second_employee + third_employee

while num_students > 0:
    time_needed += 1

    if time_needed % 4 == 0:
        continue

    num_students -= total_capacity_per_hour

print(f"Time needed: {time_needed}h.")