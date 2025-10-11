seq1 = input().split(", ")
seq2 = input().split(", ")

filtered = [word for word in seq1 if any(word in text for text in seq2)]
print(filtered)