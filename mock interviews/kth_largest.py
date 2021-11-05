import heapq

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


print(kth_largest([3,2,1,5,6,4], 2))
