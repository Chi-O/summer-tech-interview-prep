from collections import defaultdict

A = [1, 9, 8, 100, 2]

B = [2, 2, 2, 3]

C = [5, 5]

def sol(A):
    # map sum to indices of pairs
    store = defaultdict(list)

    # number of times the sum is found
    count = 1

    for i in range(len(A)):
        for j in range(i + 1, len(A)):
                this_sum = (A[i] + A[j])

                # if already in dict
                if this_sum in store:
                    for a, b in store[this_sum]:
                        # ensure that they are a different pair of numbers
                        if (a != i and a != j)  and (b != i and b != j):
                            count += 1

                # add to dict
                store[this_sum].append([A[i], A[j]])

    return (count)

print(sol(A))