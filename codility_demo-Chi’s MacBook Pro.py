"""
This is a demo task.

Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    res = 1

    while res in A:
        res += 1

    return res
def solution_2(A):
    z = list(range(1,len(A)+1))
    result = set(z).difference(set(A))
    
    return result

case_1 = [1, 3, 6, 4, 1, 2]
case_2 = [1, 2, 3]
case_3 = [-1, -3]

print(solution_2(case_1))
print(solution(case_2))
print(solution(case_3))