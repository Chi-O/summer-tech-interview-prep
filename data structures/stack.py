"""
stack data structure implemented using Python lists
all operations (except print) run in O(1) time
"""

class Stack:
  # constructor
  def __init__(self):
    self.stack = []

  # push: add item to the top(end) of the stack
  def push(self, item):
    self.stack.append(item)

  # pop: remove and return the top item
  def pop(self):
    try:
      t = self.stack[-1]
      self.stack.pop()
      return t
    except:
      print("stack is empty")

  # peek: return the top item
  def peek(self):
    try:
      t = self.stack[-1]
      return t
    except:
      print("stack is empty")
  
  # isEmpty
  def is_empty(self):
    return len(self.stack) == 0

  # size
  def size(self):
    return len(self.stack)

  #print
  def print(self):
    for item in self.stack:
      print(item, end = " " )