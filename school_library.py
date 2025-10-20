books = input().split("&")

command = input()

while command != "Done":
    action = command.split(" | ")
    do = action[0]

    if do == "Add Book":
        book_name = action[1]
        if book_name not in books:
            books.insert(0, book_name)

    elif do == "Take Book":
        book_name = action[1]
        if book_name in books:
            books.remove(book_name)
    elif do == "Swap Books":
        book1 = action[1]
        book2 = action[2]
        if book1 in books and book2 in books:
            index1 = books.index(book1)
            index2 = books.index(book2)
            books[index1], books[index2] = books[index2], books[index1]
    elif do == "Insert Book":
        book_name = action[1]
        if book_name not in books:
            books.append(book_name)
    elif do == "Check Book":
        index = int(action[1])
        if 0 <= index <= len(books):
            print(books[index])

    command = input()

print(", ".join(books))
