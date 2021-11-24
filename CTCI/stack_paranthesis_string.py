class Stack():
  # constructor
  def __init__(self):
    self.stack = []

  # push: add item to the top(end) of the stack
  def push(self, item):
    self.stack.append(item)

  # pop: remove and return the top item
  def pop(self):
    if len(self.stack) != 0:
      self.stack.pop()

  # peek: return the top item
  def peek(self):
    if len(self.stack) != 0:
      return self.stack[-1]

  # isEmpty
  def is_empty(self):
    return len(self.stack) == 0
  
def is_balanced(msg):
  comp = {}
  comp['('] = ')'
  comp[')'] = '('
  comp['['] = ']'
  comp[']'] = '['
  comp['{'] = '}'
  comp['}'] = '{'

  new = Stack()

  for ch in msg:
    if new.peek() == comp[ch]:
      new.pop()
      continue
    else:
      new.push(ch)
  
  return new.is_empty()


if __name__ == "__main__":
  should_be_false = "()(({))"

  should_be_true = "(())[[{}]]"
