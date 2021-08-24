# Database:
# put("cat", 1);
# get("cat") -> 1 
# put("dog", 2)
# get(cat) -> None
# getOrderedEntries -> [["dog", 2]]

# {"cat", LinkedList(1, next=""dog"), {"dog", LinkedList(2, next="fish")}, {"fish", LinkedList(3, next=None)}}


# {"cat", LinkedList(1, next="dog")},
# LinkedList(2)
class SLL:
    # constructor: data, next
    def __init__(self, data):
        self.data = data
        self.next = None
    
    # insert method: update next value 
    def append(self, new_key, new_data):
        new_node = SLL(new_data)
        self.next = new_key
        
        return new_node
        
        
class Dictionary:
    # constructor: key, value (SLL node)
    def __init__ (self):
        self.new_dict = {}
        
        self.head = None
        self.end = None
        
        
    # put: update key, value 
    def put(self, key, data):
        # if this is the first element
        if self.head is None:
            self.head = key
            self.end = key
            self.new_dict[key] = SLL(data)
        
        # else, add at the end
        else: 
            self.new_dict[self.end].append(key, data) 
            # self.end = key
            # insert into hashmap
    
    # get: ret
        

    

# database = Dictionary()
# database.put("cat", 1) 
# database.put("dog", 2)
        
        