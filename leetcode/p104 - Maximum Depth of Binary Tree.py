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
        depth = 0
        while stack:
            cur_depth, cur_node = stack.pop()
            depth = max(depth, cur_depth)
            for chld in cur_node.left, cur_node.right:
                if chld:
                    stack.append((cur_depth+1, chld))
        return depth
