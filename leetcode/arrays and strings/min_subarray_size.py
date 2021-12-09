class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    
        """
        return the minimal length of contiguous subsrray which sum >= target





        build sliding window while sum < target

        if sum >= target:
            res = min(end - start, res) # minimum length of subarray

            # try sliding the window
            sum -= nums[start]
            start += 1

        smallest sliding window sum = target
        [2,3,1,2,4,3]


        sum = 2

        3,1,2 
        res = 
        """
    
        res = float('inf')
        start = 0
        window_sum = 0

        for end in range(len(nums)):
            
            window_sum += nums[end]

                # shrink as much as possible before expanding window from the right
            while window_sum >= target:
                res = min((end - start + 1), res)

                window_sum -= nums[start]
                start += 1

        if res == float('inf'):
            return 0
        return res