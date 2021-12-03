class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        ## OPTIMIZED SOLUTION USING RECURSION
        
        # recursively check the left and right subtree
        
        if not p and not q:
            return True
        if not p or not q: # note that when we reach this line, we are sure that both of them are NOT empty so check return False when one of them is empty
            return False
        # when we reach this line we are sure that thye both have values, return False if they don't have the same value
        if p.val != q.val:
            return False
        
        # so they both exsist, have the same value, cehck left and right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)