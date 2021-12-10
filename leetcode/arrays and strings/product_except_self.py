"""
238. Product of Array Except Self
Medium


Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution:
    def productExceptSelf(self, nums):
        """
        [1,2,3,4]
    
        # first pass compute answer array as prefix sum
        answer[0] = 1 
        answer[i] = answer[i - 1] * nums[i - 1]
        
        # second pass:
    
        i = 2
        suffix = 4
    
        answer[i] = suffix * answer[i]
        suffix = nums[i] * suffix

        prefix//answer [1, 1, 8, 6]
        """
        # using prefix and suffix array
        answer = [0] * len(nums)
        
        # fill answer array
        answer[0] = 1
        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]

        suffix = 1
        
        # traverse answer array backwards
        for i in range(len(nums) - 1, -1, -1):
            answer[i] = suffix * answer[i]
            suffix *= nums[i] 
        
        return answer