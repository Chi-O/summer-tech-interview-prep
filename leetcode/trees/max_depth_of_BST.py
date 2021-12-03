# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # note that once we reach a node, we know that is a level so 1 + the max of the depth of its subtrees
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))