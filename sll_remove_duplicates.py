class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while(start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    # # FOR SORTED LISTS (NON-DECREASING): compare adjacent nodes and delete duplicate
    # def removeDuplicates(self, head):
    #     # if linked list is empty
    #     if head is None:
    #         return head

    #     prev = head

    #     while prev.next:
    #         # is duplicate of the next node, delete the next node
    #         if prev.data == prev.next.data:
    #             temp = prev.next.next
    #             prev.next = None
    #             prev.next = temp
    #         else:
    #             prev = prev.next

    #     return head

    # # FOR UNSORTED LISTS: store in hash and check for duplicates
    def removeDuplicates(self, head):
    # Base case of empty list or
        # list with only one element
        if self.head is None or self.head.next is None:
            return head
        
        # Hash to store seen values
        copy = set() 

        current = Node(head)

        copy.add(self.head.data)

        while current.next:
            if current.next.data in copy:
                current.next = current.next.next
            else:
                copy.add(current.next.data)
                current = current.next

        print("running")
        return head


if __name__ == "__main__":
    mylist = Solution()
    T = int(input())
    head = None

    for i in range(T):
        data = int(input())
        head = mylist.insert(head, data)

    mylist.removeDuplicates(head)
    #4
    #  mylist.display(head)
