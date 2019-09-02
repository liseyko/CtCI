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


class Solution:
    """same, but faster"""
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def dfs(r=root, path=[]):
            if not r:
                return
            path.append(str(r.val))
            if not r.left and not r.right:
                self.res.append(''.join(path))
            path.append('->')
            dfs(r.left, path)
            dfs(r.right, path)
            del path[-2:]

        self.res = []
        dfs()

        return self.res
