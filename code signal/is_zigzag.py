def isZigzag(num):
    res = []

    for i in range(1, len(num) - 1):
        res.append(int(num[i - 1] < num[i] >  num[i + 1]) or int(num[i - 1] > num[i] <  num[i + 1]))
    
    return res

print(isZigzag([1, 2, 1, 3, 4]))
print(isZigzag([1, 2, 3, 4]))
print(isZigzag([1000000000, 1000000000, 1000000000]))