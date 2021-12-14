msg = "eeccccbebaeeabebcccee"

def isPalindrome(s):
    s = list(filter(str.isalnum, s.lower()))
    
    l = 0
    r = len(s) - 1
    
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
        
    return True

print(isPalindrome(msg))