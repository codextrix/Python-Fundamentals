value = 10

print(type(value))

x, y, z, = 1, 2, 3

x = y = z = 1

text = "Exmaple"

print(text)

a = 33
b = 200

if b > a:
    print("b is more than a")

for num in range(1, 11):
    print(num)

number = 1000

if number == 1000:
    print(number)
elif number > 1000:
    print("WOW you got it stupid")
else:
    print("Error")


x = 5
y = 10
z = 15

if x < y and y < z:
    print("Blah blah")

if not x > y:
    print("pfffffffffff")

for num in range(1, 11):
    print(num)

value = list(range(1, 11))
print(value)

for _ in range(5):
    username = input()

    if username == "admin":
        print("Admin")
        break

    print(f"Welcome, {username}")


letter = "a"
for let in "bcde":
    if let == letter:
        print("Element found")
        break

else:
    print("Element not found")

i = 1
while i < 6:
    print(i)
    i += 1