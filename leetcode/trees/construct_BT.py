# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
        
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # approach:
        # root = first node in preorder
        # recusively construct the left and right subtree
        
        ind = {}
        
        for i, node in enumerate(inorder):
            ind[node] = i
        
        self.preorder_index = 0 # 0
             
        def build(left, right):
            # base case
            if left > right:
                return None
            
            # set root to first element of preorder 
            root = TreeNode(preorder[self.preorder_index])
            
            self.preorder_index += 1
            
            inorder_index = ind[root.val]
            
            root.left = build(left, inorder_index - 1)
            root.right = build(inorder_index + 1, right)
            
            return root
        
        
        return build(0, len(preorder) - 1)