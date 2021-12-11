# Squares of a Sorted Array #977

class Solution:
    def sortedSquares(self, nums):
        # first idea: change all nums to positive; but then we'd have to move the positives to the end to remain sorted
        
        # brute force; square each num and then sort // O(N log N) time, O(1) space -> we can do betterrr
        
        """
        more optimal using two-pointer
        
        start from ends and move inwards; fill answer array backwards with 
        the maximum square, and move that pointer accordingly
        
        [-7,-3,2,3,11]
               r l
        
        4  4
        
        [4,9,9,49,121]
       i
        """ 
        n = len(nums)
        l = 0
        r = n - 1
        
        # account for a one element array
        if n == 1:
            return [abs(nums[0])**2]
        
        squares = [0] * n
        i = n - 1
        
        while i >= 0 and l <= r:
            l_sq = abs(nums[l])**2
            r_sq = abs(nums[r])**2
            
            if l_sq >= r_sq:
                squares[i] = l_sq
            
                # fill the answer array backwards
                i -= 1
                
                # move inwards in the array
                l += 1
            
            else:
                squares[i] = r_sq
            
                # fill the answer array backwards
                i -= 1
                
                # move inwards in the array
                r -= 1

				# ALSO COULD PUT i -= 1 OUTSIDE CONDITIONAL SINCE WE DO IT TWICE
				# OR USE FOR LOOP TO TRAVERSE ANSWER ARRA BACKWARDS
        
        return squares