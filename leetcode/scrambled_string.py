"""
Leetcode #1160
given a list of words and input string, return the word
that can be made from the chars in the string. if more than two words, return any
"""


def scrambled(words, string):
    res = []
    present = False # assume all words are not present

    for word in words:
        for char in word:
            if string.count(char) >= word.count(char):
                present = True
            else:
                present = False
                break # this is key!!! once it doesn't have this char, we shouldn't check for others
            
        if present:
            res.append(word)

    return res

print(scrambled(["cat","bt","hat","tree"], "attach"))
print(scrambled(["hello","world","leetcode"], "welldonehoneyr"))