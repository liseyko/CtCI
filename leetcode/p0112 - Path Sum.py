class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum -= root.val
        if root.left or root.right:
            return self.hasPathSum(root.left, sum) or\
                self.hasPathSum(root.right, sum)
        return sum == 0
