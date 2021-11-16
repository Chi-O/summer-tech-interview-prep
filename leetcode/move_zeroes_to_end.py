"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Leetcode #283
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1