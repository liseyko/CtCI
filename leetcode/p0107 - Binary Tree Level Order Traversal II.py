from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # v1
    def levelOrderBottom(self, root):
        if not root:
            return []
        lvl = 1     # current level
        q = deque([root])
        ql = 1
        r = deque() # result
        clr = []    # result @ current level 

        while q:
            n = q.popleft()
            ql -= 1
            clr.append(n.val)
            for c in n.left, n.right:
                if c: 
                    q.append(c)
            if ql == 0:
                lvl += 1
                ql = len(q)
                r.appendleft(clr)
                clr = []
        return list(r)

    # v2: using list comprehensions
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """        
        if not root: return []
        res, level = deque(), deque([root])
        while level:
            res.appendleft([n.val for n in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return list(res)