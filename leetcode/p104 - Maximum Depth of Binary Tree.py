from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 1 + max(self.maxDepth(root.left),
                       self.maxDepth(root.right)) if root else 0

    def maxDepth(self, root):
        lvl, depth = [root], 0
        while any(lvl):
            lvl = [c for n in lvl for c in (n.left, n.right) if c]
            depth += 1
        return depth
