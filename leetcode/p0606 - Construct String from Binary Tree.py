class Solution:
    def tree2str(self, t: TreeNode) -> str:
        res = []
        def dfs(node=t):
            if not node:
                return 
            res.append(str(node.val))
            if node.left or node.right:
                res.append('(')
                dfs(node.left)
                res.append(')')
            if node.right:
                res.append('(')
                dfs(node.right)
                res.append(')')
        dfs()
        return ''.join(res)
