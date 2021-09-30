# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    # (1) list is empty -> return l straightaway
    if l is None:
        return l
        
    # (2) first elements = k  -> move head pointer to next element
    # if list is empty after deleting (all elements = k), break and return
    while (l and l.value == k):
        l = l.next
        if (l is None):
            return l
    
    # (3) other elements equal k -> traverse list, delete those elements
    tmp = l
    
    while tmp.next:
        if tmp.next.value == k:
            tmp.next = tmp.next.next
        else:
            tmp = tmp.next
    
    
    return l

