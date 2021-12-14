"""
Find The Duplicates

Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions: M ≈ N - the array lengths are approximately the same M ≫ N - arr2 is much bigger than arr1.
"""

def find_duplicates(arr1, arr2):
  l = 0
  r = 0
  
  answer = []
  
  while (l < len(arr1)) and (r < len(arr2)):
    if arr1[l] == arr2[r]:
      answer.append(arr1[l])
      l += 1
      r += 1
      
    elif arr1[l] < arr2[r]:
      l += 1
    
    else:
      r += 1
  
  return answer

arr1 = [11] 
arr2 = [11]
print(find_duplicates(arr1, arr2))