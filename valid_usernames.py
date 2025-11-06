def validation(username:list):
    for element in username:
        if 3<=len(element)<=16:
            if all(ch.isalnum() or ch in "-_" for ch in element):
                print(element)


usernames = input().split(", ")
valid = validation(usernames)