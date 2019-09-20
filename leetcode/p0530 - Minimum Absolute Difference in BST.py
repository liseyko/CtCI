# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stk = []
        cn = root
        b = float('-inf')
        res = float('inf')
        while cn or stk:
            while cn:
                stk.append(cn)
                cn = cn.left
            cn = stk.pop()
            a, b = b, cn.val
            res = min(res, b-a)
            cn = cn.right

        return res
