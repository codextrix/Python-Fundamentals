n = int(input())
synonyms = {}

for _ in range(n):
    word = input()
    synonym = input()

    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for word, synonym_lst in synonyms.items():
    opaaa = ", ".join(synonym_lst)
    print(f"{word} - {opaaa}")