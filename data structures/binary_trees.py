# wrapper class for tree 
class Tree:
  def __init__(self, root):
    self.root = root

  def add(self, data):
    self.root.add_node(data)

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  
  # insert method  
  # if data = node, return
  # if data < node, recurse to left and add data
  # if data > node, recurse to right and add data
  def add_node(self, data):
    if self.data == data:
      return
    
    if data < self.data:
      if self.left:
        self.left.add_node(data)
      else:
        self.left = Node(data)
    
    if data > self.data:
      if self.right:
        self.right.add_node(data)
      else:
        self.right = Node(data)

  # traversal algorithms
  # visit node, then left, then right
  def pre_order(self):
    # visit node
    print(self.data)
   
    if self.left:
      self.left.pre_order()
    
    if self.right:
      self.right.pre_order()

  # visit left, then right, then node
  def post_order(self):
    if self.left:
      self.left.post_order()
    
    if self.right:
      self.right.post_order()

    # visit node
    print(self.data)

  # visit left, then node, then right
  def in_order(self):
    if self.left:
      self.left.in_order()

    # visit node
    print(self.data)
    
    if self.right:
      self.right.in_order()


apple = Tree(Node(4))
# apple.root.add(5)
# apple.root.add(10)
# apple.root.add(76)
# apple.root.add(50)
apple.add(6)
apple.add(5)
apple.add(50)
apple.add(3)
apple.add(13)

print("in-order traversal:")
apple.root.in_order()

print("post-order traversal:")
apple.root.post_order()

print("pre-order traversal:")
apple.root.pre_order()