"""
LC #349
Intersection of Two Arrays
Easy

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.
"""

class Solution:
    def intersection(self, arr1, arr2):
        arr1.sort()
        arr2.sort()

        l = 0
        r = 0

        answer = []

        while (l < len(arr1)) and (r < len(arr2)):
            if arr1[l] == arr2[r]:
                if arr1[l] not in answer:
                    answer.append(arr1[l])
                l += 1
                r += 1

            elif arr1[l] < arr2[r]:
                l += 1

            else:
                r += 1

        return answer