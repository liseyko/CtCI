class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        def dfs(root: TreeNode, sum: int, path=[]) -> None:
            if not root:
                return
            sum, path = sum-root.val, path+[root.val]
            if not root.left and not root.right and sum == 0:
                self.res.append(path)
            else:
                dfs(root.left, sum, path)
                dfs(root.right, sum, path)

        self.res = []
        dfs(root, sum)
        return self.res
