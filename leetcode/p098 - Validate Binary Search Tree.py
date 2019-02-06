# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: 'TreeNode',
                   lt=float('inf'), gt=float('-inf')) -> 'bool':
        return not root or gt < root.val < lt\
               and self.isValidBST(root.left, min(root.val, lt), gt)\
               and self.isValidBST(root.right, lt, max(root.val, gt))
