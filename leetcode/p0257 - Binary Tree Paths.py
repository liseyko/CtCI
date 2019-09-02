class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def dfs(r=root, path=[]):
            if not r:
                return
            path.append(str(r.val))
            if not r.left and not r.right:
                self.res.append('->'.join(path))
            dfs(r.left, path)
            dfs(r.right, path)
            path.pop()

        self.res = []
        dfs()
        return self.res
