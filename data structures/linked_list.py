class Node:

  # constructor to initialize the node object
  def __init__(self, data):
    self.data = data
    self.next = None
  

# singly linked list class
class SLL:
  
  """constructor to initialize the linked list head to none (create an empty linked list)"""
  def __init__(self):
    self.head = None


  """if the head is None, the linked list is empty"""
  def is_empty(self):
    return self.head == None


  """count the number of nodes in the linked list"""
  def size(self):
    # if the list is empty, size is 0
    if self.head == None: return 0
    # otherwise, count the number of nodes
    size = 1
    current = self.head
    while current.next != None:
      size += 1
      current = current.next
    return size


  """check whether a given value is in the linked list"""
  def search(self, data):
    if self.head == None:
      return "the linked list is empty"
    
    current = self.head
    while (current.next):
      if current.data == data:
        return True
      else:
        current = current.next
      
    # did not find data
    return False
    

  """add a node at the front of the list, before the current head"""
  def prepend(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node


  """add a node after a given node"""
  def add_after(self, prev_node, new_data):
    if prev_node is None:
      print("given node is not in linked list")
      return
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node


  """add a node at the end of the list"""
  def append(self, new_data):
    new_node = Node(new_data)
    if self.head == None: 
      self.head = new_node
      return
    current = self.head
    while (current.next):
      current = current.next
    current.next = new_node

  """find and delete a given node from the list"""
  def remove(self, delete_data):
    # if the list is empty
    if self.head == None:
      return "this list is empty"
    
    # otherwise
    current = self.head

    # if the node to delete is the head
    if current.data == delete_data:
      self.head = current.next
      current = None
      return "done"

    # otherwise traverse the list, keep track of the previous 
    previous = None
    found = False

    while not found:
      # data found, delete node
      if current.data == delete_data:
        previous.next = current.next
        current = None
        return "done"

      # data not found (yet)
      else: 
        # last node reached
        if current.next == None:
          return "node not found"
        
        # check next node
        previous = current
        current = previous.next


  """print the linked list"""
  def print_list(self):
    current = self.head
    while (current):
      print(current.data, end=" ")
      current = current.next
  
  """print k-th to last element"""
  def print_k(self, head, k):
    if head is None:
      return 0

    index = self.print_k(self.head.next, k) + 1
  
    if index == k:
      print(self.head.data)
    
    return index


if __name__ == "__main__":
  new_list = SLL()

  new_list.prepend(3)
  new_list.prepend(2)
  new_list.prepend(1)

  new_list.add_after(new_list.head, 7)

  new_list.append(12)

  new_list.print_list()

  print()

  sllist = SLL()

  print(new_list.remove(2))
  print(new_list.remove(7))
  print(new_list.remove(1))
  print(new_list.remove(17))
  print(sllist.remove(17))
  new_list.print_list()