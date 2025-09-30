def calculation(operator, num1, num2):
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return int(num1 / num2)
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2

operator_ = input()
num1_ = int(input())
num2_ = int(input())

result = calculation(operator_,num1_,num2_)
print(result)