"""
DFS: use stack (iterative) or recursion to backtrack

given a binary tree and number 'S', find if the tree has a path from root-to-leaf 
such that the sum of all the node values of that path equals 'S'
"""
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, s): # returns True if path exsists, False otherwise
  # TODO: Write your code here

  if not root:
    return False

  # check if it is a leaf, and path exsists
  if root.val == s and (root.left is None) and (root.right is None):
    return True

  # recursively call the function on its left and right nodes
  # return true if either return true
  return has_path(root.left, s - root.val) or has_path(root.right, s - root.val)

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))

main()