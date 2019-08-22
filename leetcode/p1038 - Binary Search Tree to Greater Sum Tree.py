# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    val = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        self.bstToGst(root.right)
        root.val = self.val = root.val + self.val
        self.bstToGst(root.left)
        return root
