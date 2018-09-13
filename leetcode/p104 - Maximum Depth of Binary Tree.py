from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """ # Recursive
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return 1 + max( self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth(self, root):
        """ # Iterative """
        if not root:
            return 0

        q = deque([root])
        d = 0  # depth
        lq = 1 # number of nodes on each level
        
        while q:
            while lq:
                n = q.popleft()
                for c in n.left, n.right:
                    if c:
                        q.append(c)
                lq -=1

            lq = len(q)
            d += 1

        return d