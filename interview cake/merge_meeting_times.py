"""
Your company built an in-house calendar tool called HiCal. 
You want to add a feature to see the times in a day when everyone is available.
To do this, you’ll need to know when any team is having a meeting. 
In HiCal, a meeting is stored as a tuple ↴ of integers (start_time, end_time). 
These integers represent the number of 30-minute blocks past 9:00am.

Write a function merge_ranges() that takes 
a list of multiple meeting time ranges and 
returns a list of condensed ranges.

For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
 
your function would return:

  [(0, 1), (3, 8), (9, 12)]
"""

def merge_ranges(meetings):
    # sort ranges to ensure that the earliest meetings are first
    meetings.sort()

    # add first meeting to merged
    merged = [meetings[0]]

    for curr_start, curr_end in meetings[1:]:
      last_merged_start, last_merged_end = merged[-1]

      # important: at this step, we account for the case where we need a previously merged meeting time
      # update the last merged meeting time, if there is an overlap with the current one
      if curr_start <= last_merged_end:
        merged[-1] = (last_merged_start, max(last_merged_end, curr_end))
      
      # otherwise there is no overlap and we can add this to our merged array (remember that on the next iteration, when looking at the next time, this would be {merged[-1]} in case the next meeting time needs to be merged with this one)
      else:
        merged.append((curr_start, curr_end))


    return merged

example = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
case1 = [(2, 4), (3, 4), (2, 5), (8, 12), (5, 7)]
case2 = [(1, 2), (2, 3)]
case3 = [(1, 5), (2, 3)]
case4 = [(1, 10), (2, 6), (3, 5), (7, 9)]
 

print(merge_ranges(example))
print(merge_ranges(case1))
print(merge_ranges(case2))
print(merge_ranges(case3))
print(merge_ranges(case4))