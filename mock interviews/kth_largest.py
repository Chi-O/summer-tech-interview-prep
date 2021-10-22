from collections import Counter


def kthlargest(nums, k): 
    hashmap = Counter(nums)
    currentsum = 0
  # for i in list(hashmap.values()):
    print(hashmap.keys())
    print(hashmap.values())
    # i = max(hashmap, key = int) 
    # # if the value is < k 
    # if hashmap[i] < k:
    #   currentsum += hashmap[i]
    #   hashmap.pop(i)
    # 	i+=1
    # if currentsum == k:
    #   return i 


case1 = [3,2,3,1,2,4,5,5,6]
kthlargest(case1, 4)