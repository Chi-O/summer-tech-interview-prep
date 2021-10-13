def solution(A):
    # running max 
    # tuple (value, index) pair
    # initialize to the first element
    curr_max = (A[0], 0)

    # traverse the array start from the second element
    for i in range(1, len(A)):
        # if the element is greater than or equal to the curr_max
        # that element becomest the current max
        if A[i] >= curr_max[0]:
            curr_max = (A[i], i) # access the index and value together


    # return the indices *after* the max, including the max
    # nothing to the left of the max is greater than the max
    # so the max, and all the buildings to the right have an ocean view
    return list(range(curr_max[1], len(A)))

case1 = [4,2,3,1] # curr_max = (4, 0) -> wrong output of [0, 1, 2, 3]
case2 = [4,3,2,1] # [0, 1, 2, 3]
case3 = [1,3,2,4] # [3]
case4 = [2,2,2,2] # [3]

print(solution(case1))
print(solution(case2))
print(solution(case3))
print(solution(case4))