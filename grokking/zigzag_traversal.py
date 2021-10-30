"""
Given a binary tree, populate an array to represent its zigzag level order traversal. 
You should populate the values of all nodes of the first level from left to right, 
then right to left for the next level and keep alternating in the same manner for the following levels.
"""
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val

        self.left, self.right = None, None

def zig_zag_traverse(root):
    result = []

    # TODO: Write your code here

    # edge case for empty tree
    if root is None:
        return result

   # first push root
    double = deque()
    double.append(root)

    left_to_right = True # switch to alternate append direction

    while double:
        level_size = len(double)
        this_level = deque()

        for _ in range(level_size):
            curr = double.popleft()
            
            if left_to_right: # add val from the left
                this_level.append(curr.val)            
            else: # prepend val
                this_level.appendleft(curr.val)

            # add node children to deque
            if curr.left:
                double.append(curr.left)
            if curr.right:
                double.append(curr.right)
            
        left_to_right = not left_to_right
        result.append(list(this_level))

    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)

    print("Zig-zag traversal: " + str(zig_zag_traverse(root)))

main()