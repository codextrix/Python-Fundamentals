# a = 5
# b = 10
#
# result = a * b
# print(result)
#

def sum_numbers(a: int, b: int):
    return a + b


for _ in range(1, 3):
    a = int(input())
    b = int(input())

    result = sum_numbers(a, b)
    print(result)

def rechangular_area(lenght:int, width:int):
    area = lenght * width
    return area

