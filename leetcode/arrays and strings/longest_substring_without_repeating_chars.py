class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        res = 0
        chars = {}
        start = 0
        
        for end in range(len(s)):
            # if duplicate found, skip to index after most recently found
            if s[end] in chars:
                start = max(chars[s[end]] + 1, start)
            
            # keep track of the length
            res = max(res, end - start + 1)
            
            # update map
            chars[s[end]] = end
        
        return res