def check_employee_happiness(happiness_list, factor):
    improved_happiness = [current_value * factor for current_value in happiness_list]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    happy_count = sum(num >= average_happiness for num in improved_happiness)
    total_count = len(improved_happiness)

    message = "are happy" if happy_count >= total_count / 2 else "are not happy"
    return f"Score: {happy_count}/{total_count}. Employees {message}!"

happiness_lst = list(map(int, input().split()))
happiness_factor = int(input())

result = check_employee_happiness(happiness_lst, happiness_factor)
print(result)