from collections import Counter

def mostFrequentDigits(a):
    pass

a = [25, 2, 3, 57, 38, 41]

res = ""

for num in a:
    res += str(num)

print(res)

freq = dict(Counter(res))

most_freq = max(freq.values())

res = []

for dig in freq:
    if freq[dig] == most_freq:
        res.append(int(dig))

print(freq)
print(most_freq)
print(res)