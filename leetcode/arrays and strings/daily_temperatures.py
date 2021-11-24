"""
https://leetcode.com/problems/daily-temperatures/

739. Daily Temperatures
Medium

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

class Solution(object):
    # # BRUTE FORCE, so inefficient it doesn't run on LC
    # def dailyTemperatures(self, temperatures):
    #     i = 0 # 1
    #     answer = [] # [4]

    #     while i < len(temperatures):
    #         j = i + 1 # 2

    #         count = 1 # 4

    #         # warmer temperature not yet found
    #         while temperatures[j] <= temperatures[i]: # 30 < 60
    #             if j == len(temperatures) - 1:
    #                 count = 0
    #                 break

    #             else:
    #                 j += 1
    #                 count += 1

    #         answer.append(count)
    #         i += 1

    #     return answer
        
    # EFFICIENT, traverse array backwards
    # if temp[i] >= hottest: upadte hottest
    # else 
    # only check the temperatures after the temps <= the next temp 
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        ans = [0] * len(temperatures)
        hottest = 0

        for curr_day in range(len(temperatures) - 1, -1, -1):
            curr_temp = temperatures[curr_day]

            if temperatures[curr_day] >= hottest:
                hottest = temperatures[curr_day]
            else:
                days = 1
                while temperatures[curr_day + days] <=curr_temp:
                    days += ans[curr_day + days]
                ans[curr_day] = days

        return ans  