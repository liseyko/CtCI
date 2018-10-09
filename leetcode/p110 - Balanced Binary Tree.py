# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.balanced = True

    def getHeight(self, root):
        if not self.balanced:
            return -1
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        l = self.getHeight(root.left)
        r = self.getHeight(root.right)
        if abs(l - r) > 1:
           self.balanced = False

        return 1 + max(l, r)


    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.getHeight(root)
        return self.balanced