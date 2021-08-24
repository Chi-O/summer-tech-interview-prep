from collections import defaultdict

# brute force solution:
# exceeded execution time limit
# arr = [[a[i], a[j]] for i in range(len(a)) for j in range(len(a)) if (a[i] + a[j]) % k == 0 and i < j]

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 7, 9]
    k = 3

    rem = [x % k for x in a]
    index = [i for i in range(len(a))]
    # mods = list(zip(rem, index))

    s = set()

    for i in range(len(rem)):
        temp = k - rem[i]
        if temp in s:
            print("rem, complement: ", rem[i], temp)
        s.add(rem[i])
    
    

    print("rem: ", rem)
    print("ind: ", index)
    print("arr: ", a)
    # print(mods)
