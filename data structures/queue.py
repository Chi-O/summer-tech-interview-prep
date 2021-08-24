"""
queue data structure implemented using Python lists
all operations (except print) run in O(1) time
"""
class Queue:
# constructor
  def __init__(self):
    self.queue = []

# enqueue
  def add(self, item):
    self.queue.insert(0, item)

# dequeue
  def remove(self):
    try:
      print(self.queue.pop())
    except:
      print("queue is empty")

# peek
  def peek(self):
    try:
      print(self.queue[-1])
    except:
      print("queue is empty")

# size
  def size(self):
    return len(self.queue)

# is_empty
  def is_empty(self):
    return len(self.queue) == 0

# print
  def print(self):
    # for i in range(len(self.queue) -1, -1, -1):
    #   print(self.queue[i], end = " ")
    print(self.queue)

if __name__ == "__main__":
  new = Queue()

  new.add(1)
  new.add(3)
  new.add("seven")

  new.print()

  new.remove()

  new.peek()
  new.print()
  new.add('five')
  new.print()
  new.remove()
  new.print()

  """
  output:
  ['seven', 3, 1]
  1
  3
  ['seven', 3]
  ['five', 'seven', 3]
  3
  ['five', 'seven']
  """