"""
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, 
i.e., the **lowest level comes first**. 
You should populate the values of all nodes in each level from left to right in separate sub-arrays.
"""
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val

        self.left, self.right = None, None

def traverse(root):
    # NOTE: same as previous, but prepend to resulting array instead
    result = deque()

    # TODO: Write your code here

    # edge case for empty tree
    if root is None:
        return result

    # first enqueue root
    queue = deque()
    queue.append(root)

    # while the queue is not empty
    while queue:
        # get the level size
        this_level = len(queue)
        level = []

        for _ in range(this_level):
            # get the current node
            this_node = queue.popleft()

            # add the node to the current level
            level.append(this_node.val) # we want just the value

            # add the children to the queue
            if this_node.left:
                queue.append(this_node.left)
            
            if this_node.right:
                queue.append(this_node.right)
        
        # update the result array
        result.appendleft(level)

    return list(result)

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print("Reverse level order traversal: " + str(traverse(root)))

main()