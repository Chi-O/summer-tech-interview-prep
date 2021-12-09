# def solution(nums, k):
#     res = []
    
#     window_sum = 0
#     start = 0
    
#     for end in range(len(nums)):
#         window_sum += nums[end]
        
#         if end >= (k - 1):
#             res.append(window_sum / k)
            
#             # subract the element going out
#             window_sum -= nums[start]
            
#             # slide the window ahead
#             start += 1
            
#     return max(res)

def solution(nums, k):
    res = 0

    window_sum = 0
    start = 0

    for end in range(len(nums)):
        window_sum += nums[end]

        if end >= (k - 1):
            #print(window_sum)
            #print(window_sum/k)
            res = max(window_sum, res)

            # subract the element going out
            window_sum -= nums[start]

            # slide the window ahead
            start += 1
    
    print(51 / 4)
    return 

print(solution([1,12,-5,-6,50,3], 4))