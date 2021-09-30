from collections import Counter

# sort and compare
# O(N log N)
def check_permutation(str1, str2):
  if len(str1) != len(str2): return False

  return sorted(str1) == sorted(str2)


# count frequency of chars and compare
# O(S + T) time, O(S + T)
def check_permutation2(str1, str2):
  if len(str1) != len(str2): return False

  return Counter(str1) == Counter(str2)

if __name__=="__main__":
  print(check_permutation2("abc", "bac"))
