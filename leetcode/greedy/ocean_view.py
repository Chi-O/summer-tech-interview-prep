"""
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. 
Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

Example 1:
Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

Example 2:
Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.

Example 3:
Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.

Example 4:
Input: heights = [2,2,2,2]
Output: [3]
Explanation: Buildings cannot see the ocean if there are buildings of the same height to its right.

"""

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

case1 = [4,2,3,1] # curr_max = (4, 0) -> wrong output of [0, 1, 2, 3], expected output 
case2 = [4,3,2,1] # [0, 1, 2, 3]
case3 = [1,3,2,4] # [3]
case4 = [2,2,2,2] # [3

print(solution(case1))
print(solution(case2))
print(solution(case3))
print(solution(case4))