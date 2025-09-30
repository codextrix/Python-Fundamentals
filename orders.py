def order_calc(food:str, count:int):
    if food == "coffee":
        return count * 1.50
    elif food == "coke":
        return count * 1.40
    elif food == "water":
        return count * 1.00
    elif food == "snacks":
        return count * 2.00

type_food = input()
count_ = int(input())
result = order_calc(type_food,count_)
print(f"{result:.2f}")