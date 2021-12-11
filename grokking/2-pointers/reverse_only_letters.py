# Reverse Only Letters #917

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """
        reverse string in-place, skip pointer if not lowercase/uppercase
        
        j-bC-dEf-ghIa
        """
        s = list(s)
        
        l = 0
        r = len(s) - 1
        
        while l < r:
            while l < len(s) and not(s[l].isalpha()):
                l += 1
            
            while r >= 0 and not(s[r].isalpha()):
                r -= 1
            
            if l >= r:
                return "".join(s)
            
            s[l], s[r] = s[r], s[l]
            
            l += 1
            r -= 1
        
        return "".join(s)