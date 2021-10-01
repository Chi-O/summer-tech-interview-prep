"""
Write a function to check that a binary tree is a valid binary search tree.

Bonus
What if the input tree has duplicate values? -> should return False, a BST by definition has distinct values

What if -float('inf') or float('inf') appear in the input tree?
"""

class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

# RECURSIVE METHOD (much cleaner)
def is_bst(node, lower_bound = -float('inf'), upper_bound =  float('inf')):
    # base case: node is NULL (reached end of tree: return true)
    if not node:
        return True

    # check if sorting order is maintained
    if node.value >= upper_bound or node.value <= lower_bound:
        return False

    # traverse down the tree recursively
    return is_bst(node.left, lower_bound, node.value) and is_bst(node.right, node.value, upper_bound)


# root = BinaryTreeNode(70)
# root.insert_left(50)
# root.left.insert_left(100)
# root.left.insert_right(12)
# root.insert_right(13)

# print(is_bst(root, -float('inf'), float('inf'))) # returns False, as it should

root = BinaryTreeNode(5)
root.insert_left(3)
root.left.insert_left(1)
root.left.insert_right(4)
root.insert_right(7)
root.right.insert_right(float('inf'))


print(is_bst(root))