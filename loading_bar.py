def loading_bar(num) -> str:
    if num == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percent = num // 10

    return f"{num}% [{'%' * loaded_percent}{'.' * (10 -loaded_percent)}]\n Still loading..."

number = int(input())
result = loading_bar(number)
print(result)