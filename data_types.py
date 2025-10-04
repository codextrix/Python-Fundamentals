def slave(word,something):
    if word == "int":
        result_int = int(something) * 2
        return result_int
    elif word == "real":
        result_real = float(something) * 1.5
        return f"{result_real:.2f}"
    elif word == "string":
        result_string = f"${something}$"
        return result_string

string = input()
value = input()

print(slave(string,value))