"""
Medium

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.

 

Constraints:

    0 <= num <= 108

"""

def maximum_swap(n: int) -> int:
    n = list(map(int, str(n))) 

    curr_max = 0

    for i in range(1, len(n)):
        if n[i] > n[curr_max]:
            curr_max = i
        print(curr_max)

    # consider the case where the max is already the leftmost digit
    # if curr_max == 0 # the max is the leftmost digit
    # .... to find the max in the rest of the number
    
    n[0], n[curr_max] = n[curr_max], n[0]

    res = int("".join(str(x) for x in n))

    return res

print(maximum_swap(2736))