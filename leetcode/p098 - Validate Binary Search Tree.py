# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.prev = float('-inf')

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not self.isValidBST(root.left) or root.val <= self.prev:
            return False
        self.prev = root.val
        return self.isValidBST(root.right)

    def isValidBST(self, root, miN=float('-inf'), maX=float('inf')):
        if not root:
            return True
        if root.val <= miN or root.val >= maX:
            return False
        return self.isValidBST(root.left, miN, min(maX, root.val)) \
            and self.isValidBST(root.right, max(miN, root.val), maX)

    def isValidBST(self, root, left=float('-inf'), right=float('inf')):
        return not root or left < root.val < right and \
                self.isValidBST(root.left, left, root.val) and \
                self.isValidBST(root.right, root.val, right)
