class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
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
