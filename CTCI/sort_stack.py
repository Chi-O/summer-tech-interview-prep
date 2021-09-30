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
    print(self.stack)

  # SORT STACK
  def sort_stack(self):
    r = Stack()

    while not self.is_empty():
      tmp = int(self.pop())
      while (not r.is_empty()) and (int(r.peek()) > tmp):
        self.push(r.pop())
      r.push(tmp)

    while not r.is_empty():
      self.push(r.pop())
    
    print(self.stack)

if __name__ == "__main__":
  s = Stack()
  s.push(3)
  s.push(5)
  s.push(1)
  s.push(7)
  s.sort_stack()
  print(s.pop())
  print(s.peek())
  s.push(15)
  s.push(5)
  s.print()
  s.sort_stack()