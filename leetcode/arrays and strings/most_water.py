"""
Leetcode #11

11. Container With Most Water
Medium

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.


Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

"""

# brute force approach
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """

#         res = 0

#         for left in range(len(height)):
#             for right in range(left, len(height)):
#                 if height[right] <= height[left]:
#                     curr_area = height[right] * (right - left)
#                 else:
#                     curr_area = height[left] * (right - left)

#                 if curr_area >= res:
#                     res = curr_area
#         return res


# two-pointer approach
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1

        res = 0
        while left < right:
            # calculate area, update running max
            curr_area = min(height[right], height[left]) * (right - left)
           
            if curr_area >= res:
                res = curr_area
            
            # move pointer of the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            

        return res

new = Solution()
print(new.maxArea([1,8,6,2,5,4,8,3,7]))