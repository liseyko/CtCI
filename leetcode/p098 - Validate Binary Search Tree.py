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
        if not root: return True

        if not self.isValidBST(root.left) or root.val <= self.prev:
            return False
        self.prev = root.val
        return self.isValidBST(root.right)
