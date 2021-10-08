S = "performance"

def sol(S):
    store = dict()

    # for p1 in range(len(S)): 
    #     for p2 in range(len(S) - 1, -1, -1):
    #         if S[p1] == S[p2] and p1!= p2:
    #             return (S[p1: p2+1])
    p2 = len(S) - 1

    for p1 in range(len(S)):
        while p1 <= p2:
            print(p1, p2)

            p2 -= 1
            # if S[p1] == S[p2]:
            #     # print(S[p1: p2+1])
            #     print(p1, p2)
            # else:
            #     p2 -= 1

sol("performance")
# print(sol("cat"))
# print(sol("performance"))
# print(sol("cbaabaab"))