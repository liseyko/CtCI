class Solution:
    def pathSum(self, root: TreeNode, k: int):
        self.k = k
        self.d = collections.defaultdict(int, [(0, 1)])
        self.curPathSum = self.res = 0
        return self.dfs(root)

    def dfs(self, root: TreeNode) -> int:
        if not root:
            return self.res
        self.curPathSum += root.val
        complement = self.curPathSum - self.k
        if complement in self.d:
            self.res += self.d[complement]
        self.d[self.curPathSum] += 1

        self.dfs(root.left)
        self.dfs(root.right)
        self.d[self.curPathSum] -= 1
        self.curPathSum -= root.val
        return self.res
