from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        level = [root]
        while any(level):
            level = [c for n in level if n for c in (n.left, n.right)]
            for i in range(len(level) // 2):
                if getattr(level[i], 'val', None) != \
                   getattr(level[~i], 'val', None):
                    return False
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(r1, r2):
            return not r1 and not r2 or \
                   bool(r1 and r2) and r1.val == r2.val \
                   and isMirror(r1.left, r2.right) \
                   and isMirror(r2.left, r1.right)
        return isMirror(root, root)
