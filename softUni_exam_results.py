user_points_dictionary = {}
submissions_dictionary = {}
while True:
    current_result = input().split("-")
    if len(current_result) == 1:
        break  # exam finished
    elif len(current_result) == 2:  # someone is banned
        user = current_result[0]
        del user_points_dictionary[user]
    else:  # elif len(current_result) == 3
        name, course, points = current_result[0], current_result[1], int(current_result[2])
        if name not in user_points_dictionary.keys():
            user_points_dictionary[name] = 0
        if points > user_points_dictionary[name]:
            user_points_dictionary[name] = points
        if course not in submissions_dictionary.keys():
            submissions_dictionary[course] = 0
        submissions_dictionary[course] += 1
print("Results:")
for username, point in user_points_dictionary.items():
    print(f"{username} | {point}")
print("Submissions:")
for language,submissions_count in submissions_dictionary.items():
    print(f"{language} - {submissions_count}")