enqueue -> push to stack_1 

dequeue -> copy elements to stack_2 -> pop stack_2

queue = Queue()
queue.enqueue(2) // stack_1 (2)
queue.enqueue(3) // stack_1 (2, 3)
queue.enqueue(4) // stack_1 (2, 3, 4) --> stack_2 (4, 3, 2)
queue.dequeue() -> // 2 // stack_2.pop()
queue.dequeue() -> // 3

Q: implement a queue using 2 stacks

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop(-1)

class Queue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()
    
    def enqueue(self, item):
        self.stack_1.push(item)
    
    # pop all items from stack_1 and push to stack_2
    def transfer(self):
        while stack_1 is not empty:
            stack_2.push(stack_1.pop())
    
    def dequeue(self):
        
    
    

nums = [2, 7, 11, 15], target = 9
2 + 7 = 9

output: [0, 1] //index






[0, 1, 1, 2, 4, 5] -> [0, 1, 2, 4, 5]

[0, 1, 2, 2, 3, 3, 4] -> [0, 1, 2, 3, 4, __, __]

remove_dups(array):
  traverse the array
  compare each element, to the element after it:
    if equal:
      remove next element

def remove_dups(arr):
    for i in range(0, len(arr) - 2):
        if arr[i] == arr[i + 1]:
            arr[i + 1] = '__'
    
    for element in arr:
        if element != '__':
            return element