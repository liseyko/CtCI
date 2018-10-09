from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        lvl = 1
        q = deque([root])
        ql = 1

        while len(q) > 0:
            n = q.popleft()
            ql -= 1
            if n:
                if not n.left and not n.right:
                    break
                q.extend([n.left, n.right])
            if ql == 0:
                lvl += 1
                ql = len(q)

        return lvl