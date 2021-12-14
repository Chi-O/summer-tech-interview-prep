from collections import deque

"""
Implement the BSTIterator class that represents an iterator over 
the in-order traversal of a binary search tree (BST):

    BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. 
    The root of the BST is given as part of the constructor. 
    The pointer should be initialized to a non-existent number smaller than any element in the BST.

    boolean hasNext() Returns true if there exists a number in 
    the traversal to the right of the pointer, otherwise returns false.

    int next() Moves the pointer to the right, then returns the number at the pointer.

    []
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = deque()
        self.push_left(root)
        

    def next(self):
        """
        :rtype: int
        """
        result = self.stack.pop()
        self.push_left(result.right)
        return result.val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0

    
    def push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()