"""
use a single array to implement 3 stacks
"""

class MultiStack:
  def __init__(self, stack_size):
    number_of_stacks = 3
    stack_capacity = stack_size
    items = [0] *  (number_of_stacks * stack_size)
    sizes = [0] * number_of_stacks
  
  def push(self, stack_num, item):
    if is_full(stack_num):
      print("stack is full")
      return

    sizes[stack_num] += 1
    items[index_of_top(stack_num)] = item
  
  def pop(self, stack_num):
    if is_empty(stack_num):
      print("stack is empty")
      return

    top_index = index_of_top(stack_num)
    top_item = items[top_index]
    items[top_index] = 0 # clear space
    sizes[stack_num] -= 1 # shrink size

    return top_item

  def peek(self, stack_num):
    try:
      top_item = items[index_of_top(stack_num)]
      return top_item
    except:
      print("stack is empty")

  def is_full(self, stack_num):
    return sizes[stack_num] == stack_capacity

  def is_empty(self, stack_num):
    return sizes[stack_num] == 0

  def index_of_top(self, stack_num):
    offset = stack_num * stack_capacity # zero index of the current sub-stack
    last_index = sizes[stack_num] - 1 # last index of the current sub-stack
    return offset + last_index