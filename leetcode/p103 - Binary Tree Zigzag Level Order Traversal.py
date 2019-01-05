from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, q, even = [], [root], 1
        while any(q):
            if even:
                res.append([n.val for n in q if n])
            else:
                res.append([n.val for n in q[::-1] if n])
            q = [c for n in q for c in (n.left, n.right) if c]
            even = 1 - even
        return res

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, q, lvl, n, even = [], deque([root]), 0, 1, 1
        while any(q):
            r = deque([])
            print([n.val for n in q if n])
            while n:
                node = q.popleft()
                for c in (node.left, node.right):
                    if c:
                        q.append(c)
                if even:
                    r.append(node.val)
                else:
                    r.appendleft(node.val)
                n -= 1
            n = len(q)
            even = 1 - even
            res.append(list(r))
        return res
