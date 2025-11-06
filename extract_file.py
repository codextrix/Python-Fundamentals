path = input()

last_part = path.split("\\")[-1]
file_name, file_ext = last_part.rsplit(".", 1)

print(f"File name: {file_name}")
print(f"File extension: {file_ext}")