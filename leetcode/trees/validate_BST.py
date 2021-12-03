class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # for every right subtree, the parent is the lower bound (should be > parent)
        # for every left subtree, the parent is the upper bound ( should be < parent)
        
        """
        stack = [(-float("inf"), float("inf"), root)]
 
        while stack:
            lower, upper, node = stack.pop()
            
            if not (node.val < upper and node.val > lower):
                return False
            
            # check left subtree
            if node.left:
                stack.append((lower, node.val, node.left))
        
            # check right subtree
            if node.right:
                stack.append((node.val, upper, node.right))
                
        return True
        """
        
        # RECURSIVE SOLUTION
        
        
        def is_valid(node, lower, upper):
            if not node: # once we reach a leaf, we can return true
                return True
            
            if not (node.val < upper and node.val > lower):
                return False
            
            return is_valid(node.left, lower, node.val) and is_valid(node.right, node.val, upper)
            
            
        return is_valid(root, -float("inf"), float("inf"))