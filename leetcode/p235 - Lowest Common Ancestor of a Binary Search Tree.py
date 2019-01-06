# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            p, q = q, p
        while root:
            if p.val <= root.val <= q.val:
                return root
            print(root.val)
            if root.right and p.val > root.val:
                root = root.right
            else:
                root = root.left
