"""
You are given an unordered array consisting of consecutive integers [1, 2, 3, ..., n] without any duplicates. 
You are allowed to swap any two elements. 
Find the minimum number of swaps required to sort the array in ascending order
"""
# def min_swaps(arr):
#     num = 1
#     count = 0

#     while num < len(arr):
#         # print(arr, num, arr.index(num))
#         if arr.index(num) != (num - 1):
#             arr[arr.index(num)], arr[num - 1] = arr[num - 1], arr[arr.index(num)]
#             count += 1
#         num += 1

#     return count

def min_swaps(arr):
    # use hashmap to store index
    # use sorted arra yas referrence
    
    ref_arr = sorted(arr)
    index_dict = {value:index for index, value in enumerate(arr)} # map value to index
    count = 0

    for index, val in enumerate(arr):
        # get the correct value for this index using ref arr
        correct_val = ref_arr[index]

        # if this the val at this index is not the correct val
        if arr[index] != correct_val:
            i_to_swap = index_dict[correct_val] # get the index of the correct value that's supposed to be at this index, will use this to swap
            arr[index], arr[i_to_swap] = arr[i_to_swap], arr[index] # swap the values using apprpriate index
            # need to update the index dict
            index_dict[correct_val] = index
            index_dict[val] = i_to_swap
            
            count += 1
        
    return count

ex1 = [7, 1, 3, 2, 4, 5, 6]
ex2 = [4, 3, 1, 2]
ex3 = [2, 3, 4, 1, 5]
ex4 = [1, 3, 5, 2, 4, 6, 7]

print(min_swaps(ex1))
print(min_swaps(ex2))
print(min_swaps(ex3))
print(min_swaps(ex4))