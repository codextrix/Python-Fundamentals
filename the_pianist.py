def add_piece(collection_, piece_, composer_, key_):
    if piece_ in collection_:
        print(f"{piece_} is already in the collection!")
    else:
        collection_[piece_] = {"composer": composer_, "key": key_}
        print(f"{piece_} by {composer_} in {key_} added to the collection!")

def remove_pieces(collection_, piece_):
    if piece_ in collection_:
        del collection_[piece_]
        print(f"Successfully removed {piece_}!")
    else:
        print(f"Invalid operation! {piece_} does not exist in the collection.")

def change_key(collection_,piece_,  key_):
    if piece_ in collection_:
        collection_[piece_]["key"] = key_
        print(f"Changed the key of {piece_} to {key_}!")
    else:
        print(f"Invalid operation! {piece_} does not exist in the collection.")



n = int(input())
collection = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    collection[piece] = {"composer": composer, "key": key}

command = input()
while command != "Stop":
    command = command.split("|")
    action = command[0]
    if action == "Add":
        add_piece(collection, command[1], command[2], command[3])
    elif action == "Remove":
        remove_pieces(collection, command[1])
    elif action == "ChangeKey":
        change_key(collection, command[1], command[2])

    command = input()

for piece, info in collection.items():
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")



