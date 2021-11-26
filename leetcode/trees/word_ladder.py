"""
note: exceeds time limit on Leetcode, but is a general solution and works on pramp.com

"""

from collections import deque

def shortestWordEditPath(source, target, words):
    #your code goes here

    queue = deque()
    seen = set(source)

    queue.append((source, 0))

    while queue:
        word, depth = queue.popleft()
        
        if word == target:
            return depth
        
        for word2 in words:
            if one_edit(word, word2) and word2 not in seen:
                queue.append((word2, depth + 1))
                seen.add(word2)
        
    return -1
    
def one_edit(w1, w2):
    if len(w1) != len(w2):
        return False

    # flag = True
    diff = 0

    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff += 1
        
    if diff > 1:
        return False

    return True

print(shortestWordEditPath("abc", "ab", ["abc", "ab"]))