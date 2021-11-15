import heapq
import random

"""
revised solution:

(1) insert the first k elements into min heap
(2) for arr[k to n-1]:
        if arr[i] > root:
          replace root with arr[i]
          fix heap condition
(3) k-th largest is the root
"""
def kth_largest(arr, K):
  # base case
  if not arr or (K > len(arr)):
    return None

  # build min-heap from first k elements in arr
  pq = arr[0:K]
  heapq.heapify(pq)

  for i in range(K, len(arr)):
    if arr[i] > pq[0]:
      # replace root with element
      heapq.heapreplace(pq, arr[i])
  
  # return the root of the heap
  return pq[0]


# print(kth_largest([3,2,1,5,6,4], 2))

"""
another revised solution 
QuickSelect algorithm
(1) note that the index of result = len - k
(2) run QuickSelect on entire array l, r = 0, len(arr) - 1
    (1) pivot = arr[rightmost index] OR random int
        tail = leftmost index
    (2) for j in range(l, r):
          if arr[j] <= pivot:
            swap arr[j] and arr[tail]

    (3) swapping done, finally swap tail with pivot to complete partition -> now values <= pivot are to the left and values > pivot are to the right -> pivot is at the correct index
  
(3) if pivot index < k: run QuickSelect on right side (p + 1, r)
    elif pivot index > k: run QuickSelect on left side (1, p - 1)
    else pivot index == k: return arr[pivot index]
"""

def kth_largest_quick_select(arr, k):
  k = len(arr) - k

  def quick_select(arr, l, r):
    pivot = arr[r]

    tail = l

    for j in range(l, r):
      if arr[j] <= pivot:
        arr[j], arr[tail] = arr[tail], arr[j]

        tail += 1
    
    arr[tail], arr[r] = arr[r], arr[tail]

    if tail > k: 
      return quick_select(arr, l, tail - 1)
    elif tail < k: 
      return quick_select(arr, tail + 1, r)
    else: 
      return arr[tail]
  
  return quick_select(arr, 0, len(arr) - 1)

print(kth_largest_quick_select([3,2,1,5,6,4], 2))
