msg = "this is a sentence"

store = {}

for c in msg:
    if c.isalpha():
        store[c] = ord(c) - ord('a') + 1

print(store)
