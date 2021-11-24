from collections import Counter


def firstNotRepeatingCharacter(s):
  count = dict(Counter(s))

  for i in count:
    if count[i] == 1:
      return i
  
  return "_"


if __name__ == "__main__":
  s = "abacabaabacaba"

  print(firstNotRepeatingCharacter(s))