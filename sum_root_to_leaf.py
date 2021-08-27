# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # edge case where only one node in tree
        if self.is_leaf(root):
          return root.val

        path = []
        collection = []
        self.find(root, path, collection)

        print(collection)
        print(sum(collection))

    def find(self, node, path, collection):
        if node is None:
            return

        path.append(str(node.val))

        if self.is_leaf(node):
            res = self.to_string(path)
            collection.append(int(res, 2))

        self.find(node.left, path, collection)
        self.find(node.right, path, collection)

        path.pop()

    def is_leaf(self, node):
        return node.left is None and node.right is None

    def to_string(self, arr):
        return "".join(arr)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)

    sol = Solution()

    sol.sumRootToLeaf(root)
