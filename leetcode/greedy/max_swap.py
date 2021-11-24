"""
#670 Maximum Swap
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

    0 <= num <= 10^8

"""

def maximum_swap(n: int) -> int:
    n = list(map(int, str(n))) 

    curr_max = -1
    max_index = -1

    l, r = 0, 0

    for i in range(len(n) - 1, -1 , -1):
        # if num is greater than max
        if n[i] > curr_max:
            curr_max = n[i]
            max_index = i
        
        # if num is less than max, this is now the best place to swap
        elif n[i] < curr_max:
            l = i
            r = max_index
        
    # do the swap
    n[l], n[r] = n[r], n[l]


    return int("".join(str(x) for x in n))

print(maximum_swap(2736))
print(maximum_swap(98368))