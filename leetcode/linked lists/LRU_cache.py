# define DLL node object
class Node():
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = self.next = None


class LRUCache(object):
    """
    hashmap with doubly linked list
    
    map key : node
    
    head and tail nodes to keep track of the 
    most recently used (MRU) and least recently used (LRU)
    
    
    (LRU) left <-> node <-> node <-> right (MRU)
    
    
    Example 1:
    {(3, 3), (4, 4)}
    
    
    
    (LRU) left <-> (3, 3) <-> (4, 4) <-> right (MRU)
    
    """

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # init dictionary of size capacity
        # key:node
        
        self.cache = {}
        self.cap = capacity
        
        # initialize left and right nodes, connect them to each otehr
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def insert(self, node):
        # always insert node before the right pointer
        # prev <-> right
        
        node.next = self.right
        node.prev = self.right.prev
        
        self.right.prev.next = node
        self.right.prev = node
        
        
    def remove(self, node):
        # remove node from list
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # if key in dict, return node.val
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key]) # insert before right node
            
            return self.cache[key].val
        
        return -1
        
        # then node.val is MRU, insert it before right node
        
        # don't modify dictionary, change pointers in linkedlist
        # delete node, insert before right
        
        # else: return -1 (not found)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if key already exists delete that node from list then add to list at right pointer
        if key in self.cache:
            self.remove(self.cache[key])            

        # create new node, map key to node
        # add this node before right
        to_put = Node(key, value)
        self.cache[key] = to_put
        self.insert(to_put)
        
        if len(self.cache) > self.cap: # - capacity exceeded
        # remove the node after head
        # remove key val pair from dictionary
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)