from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # BFS, new array for each level, append nodes at that level
        
        res = []
        
        if not root:
            return res
        
        q = deque([root])
        
        while q:
            this_level = [] 
            
            # append all the nodes in this level
            for _ in range(len(q)):
                node = q.popleft()

                this_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(this_level)
                
        return res