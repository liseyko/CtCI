class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        maxSumLvl = (float('-inf'), -1)
        lvl, n = [root], 1
        while any(lvl):
            maxSumLvl = max(maxSumLvl, (sum(n.val for n in lvl), n))
            lvl, n = [c for n in lvl for c in (n.left, n.right) if c], n+1
        return maxSumLvl[1]
