# wrapper class for tree 
class Tree:
  def __init__(self, root):
    self.root = root

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  
  # insert method  
  # if data = node, return
  # if data < node, recurse to left and add data
  # if data > node, recurse to right and add data
  def add(self, data):
    if self.data == data:
      return
    
    if self.data < data:
      if self.left:
        self.left.add(data)
      else:
        self.left = Node(data)
    
    if self.data > data:
      if self.right:
        self.right.add(data)
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
      self.left.pre_order()
    
    if self.right:
      self.right.pre_order()

    # visit node
    print(self.data)

  # visit left, then node, then right
  def in_order(self):
    if self.left:
      self.left.pre_order()

    # visit node
    print(self.data)
    
    if self.right:
      self.right.pre_order()



apple = Tree(Node(4))
apple.root.add(5)
apple.root.add(10)
apple.root.add(76)
apple.root.add(50)
apple.root.in_order()
