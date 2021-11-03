"""
from Leetcode #1710, came up on HackerRank assessment
"""
from collections import Counter

# boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]
def maximumUnits(boxTypes, truckSize):
    """
    :type boxTypes: List[List[int]]
    :type truckSize: int
    :rtype: int
    """
    # only one box type
    if len(boxTypes) == 1:
        return ((boxTypes[0][1]) * truckSize) if (boxTypes[0][0] >= truckSize) else ((boxTypes[0][1]) * boxTypes[0][0])
    
    boxes = {} # maps value to freq
    
    for box in boxTypes:
        try: 
            boxes[box[1]] += box[0]
        except:
            boxes[box[1]] = box[0]

    boxes_ref = sorted(boxes, reverse=True)

    """prints for debugging purposes"""
    # print(boxes)
    # print(boxes_ref)

    # if truck size is 1, just take 1 of the maximum
    if truckSize == 1:
        return boxes_ref[0]
    
    # trucksize is > 1, add as much of the maximum, 
    # if still space, add as much of the next max, repeat 
    res = 0
    for box in boxes_ref:
        if truckSize >= boxes[box]:
            # print(truckSize, res, box)
            res += (box * boxes[box])
            truckSize -= boxes[box]
        else:
            # print(truckSize, res, box)
            res += (box * truckSize)
            truckSize -= truckSize

    return res

# only one box type
# print(maximumUnits([[4, 6]], 3))
# print(maximumUnits([[1, 6]], 3))
# print(maximumUnits([[3, 9]], 5))

# # # trucksize = 1
# print(maximumUnits([[4, 8], [3, 10], [1, 16], [56, 2]], 1))

# other cases
print(maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))
print(maximumUnits([[1,3],[2,2],[3,1]], 4))
print(maximumUnits([[1,3],[2,2],[3,1]], 3))
print(maximumUnits([[3,2],[1,7],[6,4]], 6))

# long case
print(maximumUnits([[2,1],[4,4],[3,1],[4,1],[2,4],[3,4],[1,3],[4,3],[5,3],[5,3]], 13))