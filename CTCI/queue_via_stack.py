"""
implement an algorithm that implements a queue using two stacks

solution:
have two stacks, stack_oldest (oldest item on top) and stack_newest (newest item on top)
a queue removes the oldest item first, so we dequeue() from stack_oldest,
after transferring all elements from stack_newest (to keep it updated)
to enqueue() we push() to stack_newest

complexity analysis:
pushing/inserting will be O(1) time as we just push to the stack
poping/removing will be O(N) time because we traverse the first stack to transfer its elements
peeking will be O(N) time for the same reason
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
      # print(item, end = " " )
      return self.stack

class MyQueue:
  def __init__(self):
    self.stack_oldest = Stack()
    self.stack_newest = Stack()
  
  def size(self):
    print(self.stack_oldest.size() + self.stack_newest.size())

  def add(self, item):
    self.stack_newest.push(item)
  
  def update(self):
    # pop elements from first stack to the other
    # only if the second stack is empty, remember that it has the elements in reverse 
    # order for dequeue() retrieval, we can always dequeue() from it (witout transfering again), 
    # as long as there is no new element added. plus the new element will be added to the old stack 
    # and we can't access the new one unless we remove the old ones. thus we only update when needed
    # i.e. if the second stack is empty

    if self.stack_oldest.is_empty():
      while (not self.stack_newest.is_empty()):
        self.stack_oldest.push(self.stack_newest.pop())

  def peek(self):
    self.update() # ensure the second self.stack is up to date
    return self.stack_oldest.peek() # return oldest item (top of queue)

  def remove(self):
    self.update() # ensure the second stack is up to date
    return self.stack_oldest.pop()

  def print(self):
    if (not self.stack_oldest.is_empty()) and (not self.stack_newest.is_empty()):
      return self.stack_newest.print() + self.stack_oldest.print()
    elif (not self.stack_newest.is_empty()):
      return self.stack_newest.print()
    else:
      return self.stack_oldest.print() 