# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        def traverse(n = root):
            if not n: return 0
            l, r = traverse(n.left), traverse(n.right)
            self.diameter = max(self.diameter, l + r)
            return 1 + max(l, r)
        traverse()

        return self.diameter