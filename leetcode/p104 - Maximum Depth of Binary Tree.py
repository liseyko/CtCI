from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    """ recursive """
    def maxDepth(self, root: TreeNode) -> int:
        return 1 + max(self.maxDepth(root.left),
                       self.maxDepth(root.right)) if root else 0

    def maxDepth(self, root: TreeNode) -> int:
        """ BFS """
        lvl, depth = [root], 0
        while any(lvl):
            lvl = [c for n in lvl for c in (n.left, n.right) if c]
            depth += 1
        return depth

    def maxDepth(self, root: TreeNode) -> int:
        """ DFS """
        stack = [(1, root)] if root else None
        result = 0
        while stack:
            depth, node = stack.pop()
            result = max(result, depth)
            stack += [(depth+1, chld)
                      for chld in (node.left, node.right) if chld]
        return result
