from collections import Counter, defaultdict


"""
Leetcode
#451. Sort Characters By Frequency
Medium

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

1) hashmap of freq
2) sort the hashmap 
3) return 

optimize:
{char : freq}

{char : index} store the first index of char
"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        count = dict()
        ind = dict()

        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
                ind[s[i]] = i

        freq = []
        for ch in count:
            elem = [ch, count[ch], ind[ch]]
            freq.append(elem)
        
        freq = sorted(freq, key=lambda elem:elem[1], reverse=True)

        for elem in freq:
            print(s[elem[2]] * elem[1], end="")


new = Solution()
new.frequencySort("treeeeee")