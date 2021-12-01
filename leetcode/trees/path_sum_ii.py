"""
#113. Path Sum II
Medium

Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. 
A leaf is a node with no children.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Time: O(N^2) because we traverse each node in the tree O(N), and potentially have to save its current path O(N)
Space: O(N) 
"""
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        
        all_paths = [] 

        get_path(root, targetSum, [], all_paths)

        return all_paths


def get_path(node, S, current_path, all_paths):
    # return when end of path reached
    if not node:
        return

    # append this node to the current path
    current_path.append(node.val)

    # found leaf, path == sum
    if node.val == S and (not node.left) and (not node.right):
        all_paths.append(list(current_path))

    # else recursively check left and right nodes
    else:
        get_path(node.right, S - node.val, current_path, all_paths) 
        get_path(node.left, S - node.val, current_path, all_paths)

    # pop the last node as we go up the recursive call stack
    current_path.pop()