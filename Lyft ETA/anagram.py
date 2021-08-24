"""
Anagram Finder
Given a list of words and an input string, output the anagrams of the input
string in the list of words

Clarification
> what is an anagram? >> a word is an anagram of another if it has the same characters with the same frequency
> what is an expected output for a given input? >> [coat, taco, race, trace] -> taco [coat]
> does it matter the order the list is returned? >> no, it doesn't matter

Algorithms
areAnagrams(word1, word2):
    sort both strings
    compare sorted strings
    
findAnagrams(list of words, input string)
for every word in the list, check if input string is an anagram
>> store in an array; append each anagram to the list
"""


def are_anagrams(word1, word2):
  # how to know runtime of a line like this 
  return sorted(word1) == sorted(word2)


# linear time complexity O(n); visits every word in the input list, and checks if it is an anagram of the input string
def find_anagram(words, target):
  anagrams = []
  for word in words:
    if are_anagrams(word, target):
      anagrams.append(word)
  return anagrams


find_anagram(['taco', 'race', 'coat', 'cat'], 'tac')


assert find_anagram(['coat', 'taco', 'car'], 'toca') == ['coat', 'taco']


# assert are_anagrams('taco', 'coat') == True
# assert are_anagrams('care', 'car') == False

